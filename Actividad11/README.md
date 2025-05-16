### Actividad: Aserciones en pruebas con pytest
**Objetivos**
- Ejecutar casos de prueba con pytest
- Identificar los casos de prueba que fallan
- Escribir pruebas unitarias utilizando aserciones
- Generar informes de cobertura usando pytest-cov

**Paso 1: Instalación de pytest y pytest-cov**

Primero creamos y activamos un entorno virtual.
```
python3 -m venv act11
```
Ahora procedemos a instalar pytest y pytest-cov
```
pip install pytest pytest-cov
```

**Paso 2: Archivos de prueba**

Usaremos dos archivos para esta actividad: `stack.py` y `test_stack.py`.

- `stack.py`: Contiene la implementación de una pila (stack) que queremos probar.
- `test_stack.py`: Contiene las pruebas para los métodos `push()`, `pop()`, `peek()`, y `is_empty()`.

Los casos de prueba se encuentran implementados en `test_stack.py` de acuerdo al archivo de `Instrucciones.md`.

Podemos ejecutar `pytest -v` para correr todas las pruebas activando la opción -v  que activa el modo detallado, mostrando que pruebas se ejecutaron y sus resultados.

En pytest, podemos usar la opción `-x` o `--exitfirst` para detener la ejecución de las pruebas al encontrar el primer fallo.

**Observaciones**:
* Ademas podemos instalar el plugin `pytest-random-order` para `pytest` que ejecuta los tests en orden aleatorio, cuyo propósito principal es detectar dependencias ocultas entre tests y que los casos de prueba no dependan del orden de ejecución.

* `unittest`: Es el módulo estándar de testing en Python, basado en el estilo de pruebas de JUnit que permite estructurar(verboso), ejecutar y reportar pruebas unitarias.
* `TestCase`: Es una clase base que proporciona métodos y utilidades para escribir pruebas que se hereda para crear clases de test personalizadas.


**Paso 3: Ejecuta pytest para verificar todas las pruebas**
Ejecutamos pytest para asegurarnos de que todas las pruebas pasan.

 <div align="center">
      <img src="https://i.postimg.cc/zB2DxqHQ/11-1.png" alt="Parte1" width="900" />
    </div>
    
**Paso 4: Agregando cobertura de pruebas con pytest-cov**

Para asegurarte de que tus pruebas cubren suficiente código, puedes generar un informe de cobertura utilizando pytest-cov. Ejecuta el siguiente comando para generar un informe de cobertura:

```
pytest --cov=stack --cov-report term-missing
```
 <div align="center">
      <img src="https://i.postimg.cc/fy3zF1xR/11-2.png" alt="Parte2" width="900" />
    </div>
    

**Paso 5: Ejecutar las pruebas usando `setup.cfg`**

Con `setup.cfg` personalizaremos cómo se ejecutan las pruebas y cómo se recopila el informe de cobertura del código. 
```py
[tool:pytest]
addopts = -v --tb=short --cov=stack --cov-report=term-missing

[coverage:run]
branch = True
omit =
    */tests/*
    */test_*

[coverage:report]
show_missing = True
```
Ahora ejecutamos todas las pruebas con esta configuracion personalizada simplemente ejecutando `pytest`
 <div align="center">
      <img src="https://i.postimg.cc/prgWtkZY/11-3.png" alt="Parte3" width="900" />
    </div>
	