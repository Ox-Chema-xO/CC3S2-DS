### Actividad: Ejecutar pruebas con pytest
Objetivos:
- Instalar pytest y pytest-cov
- Ejecutar pruebas unitarias con pytest
- Generar salida detallada y colorida para las pruebas
- Añadir informes de cobertura a los resultados de las pruebas

**Paso 1: Instalando pytest y pytest-cov**
Primero creamos y activamos un entorno virtual.
```
python3 -m venv act10
source act10/bin/activate
```
Ahora procedemos a instalar pytest y pytest-cov
```
pip install pytest pytest-cov
``` 
Esto instalará pytest para ejecutar pruebas y pytest-cov para generar informes de cobertura de código.


**Paso 2: Escribiendo y ejecutando pruebas con pytest**

pytest permite ejecutar pruebas unitarias de forma simple y estructurada sin necesidad de usar clases como en unittest. Ejecuta pytest con el siguiente comando para correr las pruebas dadas en la actividad:
Ejecutamos `pytest -v` para correr las pruebas de esta actividad.

La opción -v activa el modo detallado, mostrándote qué pruebas se ejecutaron y sus resultados. 

**Paso 3: Añadiendo cobertura de pruebas con pytest-cov**

Es importante saber cuánta parte de nuestro código está siendo cubierta por las pruebas. Para ello, usamos `pytest-cov`

- Para medir la cobertura de un módulo específico `pytest -v --cov=nombre_modulo_especifico`

- Para medir la cobertura de todo el paquete  `pytest --cov=nombre_del_paquete` 
 <div align="center">
      <img src="https://i.postimg.cc/zBs5X9Z9/10-1.png" alt="Parte1" width="900" />
    </div>

- Para generar un informe de cobertura en HTML, podemos agregar  `--cov-report=html`
 <div align="center">
      <img src="https://i.postimg.cc/J7XMd4jm/10-2.png" alt="Parte2" width="900" />
    </div>
- Para generar un informe más detallado que muestre las líneas que no están cubiertas, se agrega   `--cov-report=term-missing`


**Paso 5: Automatizando la configuración de pytest**
En lugar de escribir todos los parámetros de configuración cada vez que ejecutemos pytest, podemos guardarlos en un archivo pytest.ini o en un setup.cfg. 

**Importancia**

- setup.cfg es para múltiples herramientas como pytest, flake8, mypy, entre otros, en el proyecto, mientras que pytest.ini es solo para configurar pytest.
- En setup.cfg, las configuraciones de pytest deben ir bajo [tool:pytest].
- En pytest.ini, las configuraciones se agrupan bajo el encabezado [pytest], ya que el archivo solo es para esa herramienta.

**Paso 6: Ejecutando pruebas con la configuración automatizada**
Ahora podemos ejecutar las pruebas solo usando `pytest`.
 <div align="center">
      <img src="https://i.postimg.cc/wB3d569C/10-3.png" alt="Parte3" width="900" />
    </div>