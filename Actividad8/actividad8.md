### Actividad: El patrón Arrange-Act-Assert

#### Objetivos de aprendizaje
- Aplicar el patrón **Arrange-Act-Assert (AAA)** para estructurar pruebas unitarias claras y legibles.
- Escribir pruebas efectivas usando **Pytest**, utilizando buenas prácticas como una sola aserción por prueba.
- Comprender y aplicar los principios **FIRST** para mejorar la calidad de las pruebas.

### Estructura del proyecto
El proyecto tiene la siguiente estructura de directorios:
```
Actividad8/
├── src/
│   ├── __init__.py
|   ├── carrito.py
│   └── factories.py
├── tests/
│   └── test_carrito.py
├── requirements.txt
├── .gitignore
└── pytest.ini
```
---
### Código Fuente

El código fuente de este proyecto se encuentra en [repo-patrón-arrange-act-assert](https://github.com/Ox-Chema-xO/MiniProject-Arrange-Act-Assert).

#### Ejercicios

##### Ejercicio 1: Método para vaciar el carrito
Implementaremos el método `vaciar` el cual eliminara todos los items que se encuentren en carrito.
```py
def vaciar(self):
     """
     Vaciar la lista de items del carrito
     """
     self.items = []        
```
Implementamos el test `test_vaciar_items` para verificar que funciona correctamente nuestro método `vaciar`  y la lista de items quede vacía y el total sea 0.
```py
def test_vaciar_items():
    """
    AAA
    Arrange: Se crea un carrito y se agrega tres productos
    Act y Assert: Se verifica que al vaciar el carrito, la lista de items quede vacía y el total sea 0
    """
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Monitor", precio=300.00)
    producto2 = ProductoFactory(nombre="Televisor", precio=1300.00)
    producto3 = ProductoFactory(nombre="Dvd", precio=400.00)
    carrito.agregar_producto(producto1, cantidad=1)
    carrito.agregar_producto(producto2, cantidad=2)
    carrito.agregar_producto(producto3, cantidad=1)
    
    # Act
    carrito.vaciar()

    # Assert
    lista_items = carrito.obtener_items()
    assert len(lista_items) == 0
    assert carrito.calcular_total() == 0
```
Obteniendo los siguientes resultados:
 <div align="center">
      <img src="https://i.postimg.cc/XNQSx8VS/8-1.png" alt="Parte1" width="800" />
    </div>
    
##### Ejercicio 2: Descuento por compra mínima
Implementaremos el método `aplicar_descuento_condicional()` el cual aplicara un descuento solo si el total supera un monto determinado.
```py
    def aplicar_descuento_condicional(self, porcentaje, minimo):
        """
        Aplica un descuento condicional al total del carrito y retorna el total descontado
        solo si se supera un monto minimo
        El porcentaje debe estar entre 0 y 100
        """
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        total = self.calcular_total()
        if total >= minimo:
            return self.aplicar_descuento(porcentaje)
        return total
```
Implementamos el test `test_dscto_condicional_exitoso` para verificar que funciona correctamente nuestro método para el caso que se supera el monto minimo.
```py
def test_dscto_condicional_exitoso():
    """
    AAA
    Arrange: Se crea un carrito y se agrega dos productos
    Act y Assert: Se verifica que al aplicar el descuento condicional en el caso 
    que se supere el minimo sea correcto
    """
    #Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Monitor", precio=300.00)
    producto2 = ProductoFactory(nombre="Dvd", precio=400.00)
    carrito.agregar_producto(producto1, cantidad=1)
    carrito.agregar_producto(producto2, cantidad=1)
    
    #Act
    total_a_pagar = carrito.aplicar_descuento_condicional(porcentaje=15,minimo=500)

    #Assert
    assert total_a_pagar == 595.00
```
Implementamos el test `test_dscto_condicional_fallido` para verificar que funciona correctamente nuestro método para el caso que no se supera el monto minimo.
```py
def test_dscto_condicional_fallido():
    """
    AAA
    Arrange: Se crea un carrito y se agrega un producto
    Act y Assert: Se verifica que al aplicar el descuento condicional en el caso 
    que no se supere el minimo se retorne el total
    """
    #Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Monitor", precio=300.00)
    carrito.agregar_producto(producto1, cantidad=1)
    
    #Act
    total_a_pagar = carrito.aplicar_descuento_condicional(porcentaje=15,minimo=500)

    #Assert
    assert total_a_pagar == 300.00
```
Obteniendo los siguientes resultados:
<div align="center">
      <img src="https://i.postimg.cc/qqyjd9km/8-2.png" alt="Parte8-2" width="800" />
    </div>

##### Ejercicio 3: Manejo de stock en producto
Actualizamos la clase Producto para que incluya stock
```py
lass Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __repr__(self):
        return f"Producto({self.nombre}, precio = {self.precio}, stock = {self.stock})"
```
Modificamos ProductoFactory para que se genere un stock aleatorio entre 1 y 100
```py
# src/factories.py
import factory
from .carrito import Producto
class ProductoFactory(factory.Factory):
    class Meta:
        model = Producto
    nombre = factory.Faker("word")
    precio = factory.Faker("pyfloat", left_digits=2, right_digits=2, positive=True)
    stock = factory.Faker("pyint", min_value=1, max_value=100)
```
Actualizamos el metodo `agregar_producto`, para solo aplicarlo si hay stock del producto.
```py
    def agregar_producto(self, producto, cantidad):
        """
        Agrega un producto al carrito. Si el producto ya existe, incrementa la cantidad.
        siempre y cuando la suma de cantidades no supere el stock del producto.
        """
        for item in self.items:
            if item.producto.nombre == producto.nombre: 
                if item.cantidad + cantidad > producto.stock:
                    raise ValueError("No hay suficiente stock")
                item.cantidad += cantidad
                return
        if cantidad > producto.stock:
            raise ValueError("No hay suficiente stock")
        self.items.append(ItemCarrito(producto, cantidad))
```
Creamos el siguiente test `test_agregar_producto_dentro_de_stock()` para verificar los casos exitosos
```py
def test_agregar_producto_dentro_de_stock():
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item con el producto y la cantidad
    dentro del rango de stock
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Laptop", precio=1000.00, stock=7)
    
    # Act
    carrito.agregar_producto(producto,cantidad=5)
    
    # Assert
    item = carrito.obtener_items().pop()
    assert item.producto.nombre == "Laptop"
    assert item.cantidad == 5
```
Luego creamos el siguiente test `test_agregar_producto_fuera_de_stock()` para los casos fallidos.
```py
def test_agregar_producto_fuera_de_stock():
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que se lanza un error al intentar agregar un producto
    con cantidad superior al stock
    """
    # Arrange
    carrito = Carrito()
    producto = ProductoFactory(nombre="Laptop", precio=1000.00, stock=7)
    
    # Act y Assert
    with pytest.raises(ValueError):
        carrito.agregar_producto(producto, cantidad=8)
```
Obteniendo los siguientes resultados:
<div align="center">
      <img src="https://i.postimg.cc/kXPTyXcL/8-3.png" alt="Parte8-3" width="800" />
    </div>

##### Ejercicio 4: Ordenar items del carrito
Agregamos un método `obtener_items_ordenados` en `Carrito` que utiliza la función `sorted()` con una función lambda para ordenar según el criterio elegido, para este caso nombre y precio.
```py
 def obtener_items_ordenados(self, criterio:str):
    if criterio.lower() == "precio":
        return sorted(self.items, key=lambda item: item.producto.precio)
    elif criterio.lower() == "nombre":
        return sorted(self.items, key=lambda item: item.producto.nombre)
    else:
        return self.items
```
Ahora creamos un test `test_obtener_items_ordenados_por_criterio` para verificar que los items esten correctamente ordenados según el criterio utilizado
```py
def test_obtener_items_ordenados_por_criterio():
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Monitor", precio=300.00)
    producto2 = ProductoFactory(nombre="Televisor", precio=1300.00)
    producto3 = ProductoFactory(nombre="Dvd", precio=400.00)
    carrito.agregar_producto(producto1, cantidad=1)
    carrito.agregar_producto(producto2, cantidad=1)
    carrito.agregar_producto(producto3, cantidad=1)
    
    # Act
    items_ordenados_por_nombre = carrito.obtener_items_ordenados("nombre")
    items_ordenados_por_precio = carrito.obtener_items_ordenados("Precio")

    # Assert
    assert [item.producto.nombre for item in items_ordenados_por_nombre] == ["Dvd","Monitor","Televisor"]
    assert [item.producto.precio for item in items_ordenados_por_precio] == [300.00, 400.00, 1300.00]
```
Obteniendo los siguientes resultados:
<div align="center">
      <img src="https://i.postimg.cc/nhHT6RNk/8-4.png" alt="Parte8-4" width="800" />
    </div>


##### Ejercicio 5: Uso de Pytest Fixtures
Me permite centralizar y reutilizar la creación y configuración de objetos comunes en tus tests.
Crearemos el archivo `tests/conftest.py` para reutilizar la creacion  y configurauracion repetitiva de Carrito o producto, para centrarnos exclusivamente en las pruebas.

**Objetivo:**  
Refactoriza las pruebas para que utilicen **fixtures** de Pytest, de modo que se reutilicen instancias comunes de `Carrito` o de productos.

**Pistas:**
- En el archivo `tests/conftest.py`, crea una fixture para un carrito vacío:
  ```python
  import pytest
  from src.carrito import Carrito

  @pytest.fixture
  def carrito():
      return Carrito()
  ```
- Crea también una fixture para un producto genérico, usando la fábrica:
  ```python
  import pytest
  from src.factories import ProductoFactory

  @pytest.fixture
  def producto_generico():
      return ProductoFactory(nombre="Genérico", precio=100.0)
  ```
Por ejemplo actualizaremos 
`test_agregar_producto_dentro_de_stock()`
```py
def test_agregar_producto_dentro_de_stock(carrito, producto_generico):
    """
    AAA:
    Arrange: carrito y producto ya estan listos por fixture
    Act:
    Assert: 
    """
    # Arrange
    # carrito y producto ya estan listos por fixture
    # producto generico cuenta con una cantidad en stock de 7
    # Act
    carrito.agregar_producto(producto_generico,cantidad=5)
    
    # Assert
    item = carrito.obtener_items().pop()
    assert item.cantidad == 5
```
Obteniendo los siguientes resultados
<div align="center">
      <img src="https://i.postimg.cc/N0FD0ys2/8-5.png" alt="Parte8-5" width="800" />
    </div>

##### Ejercicio 6: Pruebas parametrizadas
Utilizaremos `@pytest.mark.parametrize` para verificar múltiples casos en un solo test, mantiendo un codigo mas limpio.
Por ejemplo, en el siguiente test.
```py
@pytest.mark.parametrize(
    "cantidad, porcentaje, minimo, esperado",
    [
        (1, 10, 200, 100),
        (2, 10, 200, 180),
        (3, 20, 250, 240),
    ]
)
def test_dscto_condicional_varios_casos(
    carrito, producto_generico, cantidad, porcentaje, minimo, esperado
):
    # Arrange: producto_generico tiene un precio de 100 y stock 7
    carrito.agregar_producto(producto_generico, cantidad=cantidad)

    # Act
    total_a_pagar = carrito.aplicar_descuento_condicional(porcentaje, minimo)

    # Assert
    assert total_a_pagar == esperado
```
Obteniendo los siguientes resultados:
<div align="center">
      <img src="https://i.postimg.cc/6QP049qj/8-6.png" alt="Parte8-6" width="800" />
    </div>

##### Ejercicio 7: Calcular impuestos en el carrito
Implementaremos el método `calcular_impuestos(porcentaje)` para retornar  el valor del impuesto calculado sobre el total del carrito, siguiendo el flujo Red‑Green‑Refactor(RGR)

- **Red**: Escribiremos un test que falle debido a que no cumplimos el nuevo requisito.
```py
def test_calcular_impuestos(carrito, producto_generico):
    """
    Red: Se espera que calcular_impuestos retorne el valor del impuesto.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=4)
    
    # Act
    impuesto = carrito.calcular_impuestos(10)  

    # Assert
    assert impuesto == 40.00
```
<div align="center">
      <img src="https://i.postimg.cc/MTkB8XvS/8-7-1.png" alt="Parte8-7-1" width="800" />
    </div>
    
- **Green**: Modificaremos `carrito.py ` para que el test pase de la forma más sencilla posible.
```py
    def calcular_impuestos(self, porcentaje):
        total = self.calcular_total()
        return total * (porcentaje / 100)
```
- **Refactor**: Mejoraremos el codigo para que sea mas legible o eficiente sin romper el test.
Agregamos documentacion y validacion de porcentaje en `carrito.py ` 
```py
    def calcular_impuestos(self, porcentaje):
        """
        Calcula el valor de los impuestos basados en el porcentaje indicado.
        
        Args:
            porcentaje (float): Porcentaje de impuesto a aplicar (entre 0 y 100).
        
        Returns:
            float: Monto del impuesto.
        
        Raises:
            ValueError: Si el porcentaje no está entre 0 y 100.
        """
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        total = self.calcular_total()
        return total * (porcentaje / 100)
```
Obteniendo los siguientes resultados:
<div align="center">
      <img src="https://i.postimg.cc/2Ssy1Mmd/8-7-2.png" alt="Parte8-7-2" width="800" />
    </div>


##### Ejercicio 8: Aplicar cupón de descuento con límite máximo
Implementaremos un método `aplicar_cupon(descuento_porcentaje, descuento_maximo)` que aplique un cupón de descuento al total del carrito, siempre y cuando el descuento no supere un valor máximo, para ello seguiremos el flujo RGR.
- **Red**: Escribiremos un test que falle debido a que no cumplimos el nuevo requisito.
```py
def test_aplicar_cupon_con_limite(carrito, producto_generico):
    """
    Red: Se espera que al aplicar un cupón, el descuento no supere el límite máximo.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=5)

    # Act
    total_con_cupon = carrito.aplicar_cupon(20, 50) 

    # Assert
    assert total_con_cupon == 450.00
```
<div align="center">
      <img src="https://i.postimg.cc/65TpYtpL/8-8-1.png" alt="Parte8-8-1" width="800" />
    </div>
    
- **Green**: Modificaremos `carrito.py ` para que el test pase de la forma más sencilla posible.
```py
def aplicar_cupon(self, descuento_porcentaje, descuento_maximo):
    total = self.calcular_total()
    descuento_calculado = total * (descuento_porcentaje / 100)
    descuento_final = min(descuento_calculado, descuento_maximo)
    return total - descuento_final
```

- **Refactor**: Mejoraremos el codigo para que sea mas legible sin romper el test.
Por ello agregamos documentacion y validacion de porcentaje en `carrito.py ` 
```py
    def aplicar_cupon(self, descuento_porcentaje, descuento_maximo):
        """
        Aplica un cupón de descuento al total del carrito, asegurando que el descuento no exceda el máximo permitido.
        
        Args:
            descuento_porcentaje (float): Porcentaje de descuento a aplicar.
            descuento_maximo (float): Valor máximo de descuento permitido.
        
        Returns:
            float: Total del carrito después de aplicar el cupón.
        
        Raises:
            ValueError: Si alguno de los valores es negativo.
        """
        if descuento_porcentaje < 0 or descuento_maximo < 0:
            raise ValueError("Los valores de descuento deben ser positivos")
        
        total = self.calcular_total()
        descuento_calculado = total * (descuento_porcentaje / 100)
        descuento_final = min(descuento_calculado, descuento_maximo)
        return total - descuento_final
```
Obteniendo los siguientes resultados:
 <div align="center">
      <img src="https://i.postimg.cc/5t6xvLfB/8-8-2.png" alt="Parte8-8-2" width="800" />
    </div>

##### Ejercicio 9: Validación de stock al agregar productos (RGR)
Nos aseguraremos que al agregar un producto al carrito, no se exceda la cantidad disponible en stock usando el flujo RGR.
- **Red**: Creamos un test que falle debido a que no cumplimos el nuevo requisito.
```py
def test_agregar_producto_excede_stock():
    """
    Red: Se espera que al intentar agregar una cantidad mayor a la disponible en stock se lance un ValueError.
    """
    # Arrange: Se crea un producto y un carrito
    # Suponemos que el producto tiene 5 unidades en stock.
    
    producto = Producto("ProductoStock", 100.00, 5)
    carrito = Carrito()

    # Act & Assert
    with pytest.raises(ValueError):
        carrito.agregar_producto(producto, cantidad=6)
```
- **Green**: Modificaremos el método `agregar_producto` de `carrito.py ` para que el test pase de la forma más sencilla posible.
```py
    def agregar_producto(self, producto, cantidad):
        """
        Agrega un producto al carrito. Si el producto ya existe, incrementa la cantidad.
        siempre y cuando la suma de cantidades no supere el stock del producto.
        """
        for item in self.items:
            if item.producto.nombre == producto.nombre: 
                if item.cantidad + cantidad > producto.stock:
                    raise ValueError("No hay suficiente stock")
                item.cantidad += cantidad
                return
        if cantidad > producto.stock:
            raise ValueError("No hay suficiente stock")
        self.items.append(ItemCarrito(producto, cantidad))
```
- **Refactor:**  
   - Centralizaremos la validación del stock, creando un método `verificar_stock`que usaremos en `agregar_producto` 
   - Documentaremos los métodos
   
   
````py
def verificar_stock(self, producto, cantidad):
        """
        Verifica si la cantidad a agregar supera el stock del producto, de ser asi lanza una excepcion,
        en caso contrario retorna la cantidad actual del producto.
        """
        stock_actual = 0
        cantidad_actual = 0
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                cantidad_actual = item.cantidad
                stock_actual = producto.stock - cantidad_actual
                if cantidad > stock_actual:
                    raise ValueError(f"No hay suficiente stock, el stock actual del producto es {stock_actual}")
                break
        if cantidad > producto.stock:
            raise ValueError(f"No hay suficiente stock, el stock actual del producto es {producto.stock}")
        
        return cantidad_actual
                       
def agregar_producto(self, producto, cantidad):
    """
    Agrega un producto al carrito. Si el producto ya existe, incrementa la cantidad.
    siempre y cuando la suma de cantidades no supere el stock del producto.
    """
    cantidad_actual = self.verificar_stock(producto,cantidad)

    for item in self.items:
        if item.producto.nombre == producto.nombre:
            nueva_cantidad = cantidad_actual + cantidad
            self.actualizar_cantidad(producto, nueva_cantidad)
            return
    self.items.append(ItemCarrito(producto, cantidad))
   ````
   Obteniendo los siguientes resultados:
   <div align="center">
      <img src="https://i.postimg.cc/qMYMFStf/8-9-1.png" alt="Parte8-9-1" width="800" />
    </div>
   
   <div align="center">
      <img src="https://i.postimg.cc/W1kbc8rd/8-9-2.png" alt="Parte8-9-2" width="800" />
    </div>
