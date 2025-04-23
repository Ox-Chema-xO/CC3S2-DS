
### Actividad: Pruebas BDD con behave en español

### Estructura del proyecto

El proyecto tiene la siguiente estructura de directorios:
```
.
├── src/
│   ├── belly.py
│   └── clock.py
├── test/
│   └── test_belly.py
├── features/
│   ├── belly.feature
│   ├── environment.py
│   └── steps/
│       └── belly_steps.py
├── requirements.txt 
└── .gitignore

```


#### Ejercicio 1: **Añadir soporte para minutos y segundos en tiempos de espera**
   <div align="center">
      <img src="https://i.postimg.cc/Dz4rBjBt/7-1.png" alt="Parte1" width="600" />
    </div>
       <div align="center">
      <img src="https://i.postimg.cc/J4tGNyTF/7-1-1.png" alt="Parte1" width="600" />
    </div>


#### Ejercicio 2: **Manejo de cantidades fraccionarias de pepinos**
   <div align="center">
      <img src="https://i.postimg.cc/SN8j10hL/7-2.png" alt="Parte1" width="600" />
    </div>

#### Ejercicio 3: **Soporte para idiomas múltiples (Español e Inglés)**
   <div align="center">
      <img src="https://i.postimg.cc/NjkFY1L5/7-3.png" alt="Parte1" width="600" />
    </div>



#### Ejercicio 4: **Manejo de tiempos aleatorios**
   <div align="center">
      <img src="https://i.postimg.cc/Qt2hctV2/7-4.png" width="600" />
    </div>

#### Ejercicio 5: **Validación de cantidades no válidas**
 <div align="center">
      <img src="https://i.postimg.cc/05S8PpBP/7-5.png" alt="Parte1" width="600" />
    </div>


#### Ejercicio 6: **Escalabilidad con grandes cantidades de pepinos**
  <div align="center">
      <img src="https://i.postimg.cc/DzmTDsGV/7-6.png" alt="Parte1" width="600" />
    </div>


#### Ejercicio 7: **Descripciones de tiempo complejas**
<div align="center">
      <img src="https://i.postimg.cc/1tqZRQMJ/7-7.png" alt="Parte1" width="600" />
    </div>

#### Ejercicio 8: **De TDD a BDD – Convertir requisitos técnicos a pruebas en Gherkin**
 <div align="center">
      <img src="https://i.postimg.cc/gjbbnTTd/7-8.png" alt="Parte1" width="600" />
    </div>

#### Ejercicio 9: **Identificación de criterios de aceptación para historias de usuario**
   <div align="center">
		  <img src="https://i.postimg.cc/7PSypq5L/7-9.png" alt="Parte1" width="600" />
</div>



#### Ejercicio 10: **Escribir pruebas unitarias antes de escenarios BDD**
   <div align="center">
      <img src="https://i.postimg.cc/yYBzK2Ry/7-10.png" alt="Parte1" width="600" />
    </div>
       <div align="center">
      <img src="https://i.postimg.cc/PqCgKHGT/7-10-1.png" alt="Parte1" width="600" />
    </div>

#### Ejercicio 11: **Refactorización guiada por TDD y BDD**
   <div align="center">
      <img src="https://i.postimg.cc/LsGrbWRf/7-11.png" alt="Parte1" width="600" />
    </div>


#### Ejercicio 12: **Ciclo completo de TDD a BDD – Añadir nueva funcionalidad**
<div align="center">
      <img src="https://i.postimg.cc/Ss8wFGNP/7-12.png" alt="Parte1" width="600" />
    </div>
    <div align="center">
      <img src="https://i.postimg.cc/1Xr245Fc/7-12-1.png" alt="Parte1" width="600" />
    </div>

#### Ejercicio 13: **Añadir criterios de aceptación claros**
 <div align="center">
      <img src="https://i.postimg.cc/qMQWTq4p/7-13.png" alt="Parte1" width="600" />
    </div>

#### Ejercicio 14: **Integración con Mocking, Stubs y Fakes (para DevOps)**
 <div align="center">
      <img src="https://i.postimg.cc/MGfLVYRG/7-14.png" alt="Parte1" width="600" />
    </div>


#### Ejercicio 15: **Despliegue y validación continua en un entorno de integración (CI/CD)**

```yml
name: CI Belly

on:
  push:
    branches: [main]
    paths:
      - 'Actividades/Actividad7/**'
  pull_request:
    branches: [main]
    paths:
      - 'Actividades/Actividad7/**'

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest behave flake8
          pip install -r Actividades/Actividad7/requirements.txt || true

      - name: Verificar formato de codigo con flake8
        run: |
          echo "Verificando calidad del codigo con flake8..."
          flake8 Actividades/Actividad7/src/ Actividades/Actividad7/test/ Actividades/Actividad7/features/steps/ --max-line-length=100

  tests_unitarios:
    runs-on: ubuntu-latest
    needs: build

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest

      - name: Ejecutar pruebas unitarias con Pytest
        run: |
          echo "Ejecutando pruebas unitarias..."
          pytest Actividades/Actividad7/test/

  tests_bdd:
    runs-on: ubuntu-latest
    needs: build

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install behave

      - name: Ejecutar pruebas BDD
        run: |
          echo "Ejecutando pruebas BDD con behave..."
          behave Actividades/Actividad7/features/ --no-capture --no-capture-stderr


```



