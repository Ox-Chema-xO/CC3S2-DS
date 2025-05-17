### Actividad: Revisión de fixtures en pruebas
Los **fixtures** proporcionan un contexto definido, confiable y consistente para las pruebas. Definen los pasos y datos de la fase `arrange` de una prueba. 
Se pueden reutilizar y usar es distintas pruebas, ademas permiten establecer y limpiar el estado antes y después de las pruebas, facilitando en general, la preparación del entorno de pruebas.

En esta actividad:
- Usaremos`@pytest.fixture(scope="module")`para ejecutar codigo una vez antes de todas las pruebas de un módulo.
 
- Usaremos los métodos `setup_class` y `teardown_class` para ejecutar codigo una vez por clase de prueba.

- Usaremos los métodos`setup_method` y  `teardown_method` para ejecutar codigo antes y después de cada prueba individual.

Observación: `yield`  separa el código en dos partes: el código que esta antes del `yield` se ejecuta  antes de las pruebas  y el código que esta despues del `yield` se ejecuta después de las pruebas.


### **Inicializar la base de datos**

Configuramos un fixture de prueba para conectar y desconectar de la base de datos. Esto solo debe hacerse una vez antes de todas las pruebas y una vez después de todas las pruebas. Por lo cual crearemos un fixture que ejecute estas acciones a nivel de módulo.

```python
import pytest
from models import db  # Asegúrate de que db está correctamente importado

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Configura la base de datos antes y después de todas las pruebas"""
    # Se ejecuta antes de todas las pruebas
    with app.app_context():
        db.create_all()
        yield
        # Se ejecuta después de todas las pruebas
        db.session.close()
```

Este fixture se ejecutará automáticamente antes de todas las pruebas del módulo y cerrará la sesión de la base de datos al finalizar todas las pruebas.

### **Cargar datos de prueba**

Cargamos algunos datos de prueba que serán usados durante las pruebas. Esto solo necesita hacerse una vez antes de todas las pruebas de la clase de pruebas.

```python
class TestAccountModel:
    """Modelo de Pruebas de Cuenta"""

    @classmethod
    def setup_class(cls):
        """Conectar y cargar los datos necesarios para las pruebas"""
        global ACCOUNT_DATA
        with open('tests/fixtures/account_data.json') as json_data:
            ACCOUNT_DATA = json.load(json_data)
        print(f"ACCOUNT_DATA cargado: {ACCOUNT_DATA}")

```

Este método se ejecuta una vez antes de todas las pruebas de la clase, cargando los datos de prueba necesarios.

### **Escribir un caso de prueba para crear una cuenta**
Escribimos un caso de prueba que cree una cuenta y luego llame al método `Account.all()` para asegurar que se devuelve una cuenta.
```python
def test_create_an_account(self):
    """Probar la creación de una sola cuenta"""
    data = ACCOUNT_DATA[0]  # obtener la primera cuenta
    account = Account(**data)
    account.create()
    assert len(Account.all()) == 1
```
Este método crea una cuenta utilizando los datos de prueba y verifica que hay exactamente una cuenta en la base de datos.

### Escribir un caso de prueba para crear todas las cuentas**

Ahora escribimos una prueba que cree todas las cuentas del diccionario `ACCOUNT_DATA`.
```python
def test_create_all_accounts(self):
    """Probar la creación de múltiples cuentas"""
    for data in ACCOUNT_DATA:
        account = Account(**data)
        account.create()
    assert len(Account.all()) == len(ACCOUNT_DATA)
```
Este método crea todas las cuentas de los datos de prueba y verifica que el número de cuentas en la base de datos coincide con el número de cuentas en `ACCOUNT_DATA`.

### ** Limpiar las tablas antes y después de cada prueba**

Para evitar que las pruebas fallen debido a que las pruebas anteriores están afectando el resultado de las siguientes pruebas, agregamos los siguientes métodos que limpien las tablas antes y después de cada prueba.
```python
def setup_method(self):
    """Truncar las tablas antes de cada prueba"""
    db.session.query(Account).delete()
    db.session.commit()

def teardown_method(self):
    """Eliminar la sesión después de cada prueba"""
    db.session.remove()
```

Estos métodos aseguran que la base de datos esté limpia antes y después de cada prueba, evitando que los datos residuales afecten a las pruebas subsecuentes.

#### Ejecutar las pruebas
Ejecutamos las pruebas para asegurarnos que todas pasen exitosamente.
 <div align="center">
      <img src="https://i.postimg.cc/HLkhQhFS/12-1.png" alt="Pruebas" width="900" />
    </div>
	