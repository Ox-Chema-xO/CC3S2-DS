
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
Para ello extendemos  la expresion regular para poder captar los segundos y lo agregamos en seconds_word para calcularlo en el total de horas.
```py
pattern = re.compile(
        r'(?:(\w+)\s*horas?)?\s*(?:(\w+)\s*minutos?)?\s*(?:(\w+)\s*segundos?)?'
        )
```
Entonces nuestra funcion queda de esta forma.
```py
@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    time_description = time_description.strip('"').lower()
    time_description = time_description.replace('y', ' ')
    time_description = time_description.replace(',', ' ')
    time_description = time_description.strip()

    if time_description == 'media hora':
        total_time_in_hours = 0.5
    else:
        pattern = re.compile(
        r'(?:(\w+)\s*horas?)?\s*(?:(\w+)\s*minutos?)?\s*(?:  (\w+)\s*segundos?)?'
        )
        match = pattern.match(time_description)

        if match:
            hours_word = match.group(1) or "0"
            minutes_word = match.group(2) or "0"
            seconds_word = match.group(3) or "0"

            hours = convertir_palabra_a_numero(hours_word)
            minutes = convertir_palabra_a_numero(minutes_word)
            seconds = convertir_palabra_a_numero(seconds_word)
            total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
        else:
            raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

    context.belly.esperar(total_time_in_hours)
```
Ahora creamos el siguiente test unitario para validar el correcto funcionamiento de esta funcion.
```py
@pytest.mark.parametrize("entrada,esperado", [
	("90 minutos", 1.5),
	("3600 segundos", 1.0),
	("1 hora y 30 minutos", 1.5),
	("1 hora y 30 minutos y 45 segundos", 1.5125),
	("media hora", 0.5),
])
def  test_convertir_tiempo_a_horas(entrada, esperado):
	resultado  =  convertir_tiempo_a_horas(entrada)
	assert  round(resultado, 4) ==  round(esperado, 4)
```
Ahora planteamos y verificamos que cumpla el siguiente scenario.
   <div align="center">
      <img src="https://i.postimg.cc/Dz4rBjBt/7-1.png" alt="Parte1" width="600" />
    </div>
Finalmente corremos el test.
   <div align="center">
      <img src="https://i.postimg.cc/J4tGNyTF/7-1-1.png" alt="Parte1" width="600" />
    </div>


#### Ejercicio 2: **Manejo de cantidades fraccionarias de pepinos**
Para ello usamos el type convert, float en formato general `g`
```py
@given('que he comido {cukes:g} pepinos')
def  step_given_eaten_cukes(context, cukes):
context.belly.comer(float(cukes))
```
   <div align="center">
      <img src="https://i.postimg.cc/SN8j10hL/7-2.png" alt="Parte1" width="600" />
    </div>

#### Ejercicio 3: **Soporte para idiomas múltiples (Español e Inglés)**
Para este ejercicio, modificamos nuestra funcion `convertir_palabra_a_numero`, agregando el siguiente diccionario `numeros_en`.
```py
numeros_en  = {

"zero": 0, "one": 1, "a": 1, "an": 1, "two": 2, "three": 3, "four": 4, "five": 5,"six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, 
"eleven": 11,"twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen":15,
"sixteen": 16,"seventeen": 17, "eighteen": 18, "nineteen": 19,
"twenty": 20, "thirty": 30,"forty": 40, "fifty": 50, "sixty": 60,
"seventy": 70, "eighty": 80, "ninety": 90,"half": 0.5
}

```
Luego en la funcion `convertir_tiempo_a_horas` extendemos la expresion regular para que soporte hours, minutes y seconds.
```py
    pattern = re.compile(
        r'(?:(\w+)\s*(horas?|hours?))?\s*(?:(\w+)\s*(minutos?|minutes?))?\s*(?:(\w+)\s*(segundos?|seconds?))?'
    )
```
Planteamos el siguiente scenario en gherkin.

   <div align="center">
      <img src="https://i.postimg.cc/NjkFY1L5/7-3.png" alt="Parte1" width="600" />
    </div>

#### Ejercicio 4: **Manejo de tiempos aleatorios**
Creamos una funcion en la cual generar un tiempo aleatorio para un rango dado, cuyo minimo es 1, por ejemplo de 1 a 3, en el cual usamos regex para extraer el rango de horas, ademas para ello estamos considerado que el rango debe ser numerico , es decir no mediante palabras. 
```py
def  generar_tiempo_aleatorio(texto):
texto  =  texto.lower().strip()
match  =  re.match(r"(?:un\s+tiempo\s+aleatorio\s+)?(entre|between)\s+([\d\.]+)\s+(y|and)\s+([\d\.]+)\s+(horas?|hours?)",texto)
if  match:
	min_horas  =  float(match.group(2)) or  "0"
	max_horas  =  float(match.group(4)) or  "0"
	return  round(random.uniform(min_horas+0.5,max_horas), 2)
return  None
```
El scenario en gherkin.
   <div align="center">
      <img src="https://i.postimg.cc/Qt2hctV2/7-4.png" width="600" />
    </div>

#### Ejercicio 5: **Validación de cantidades no válidas**
Para ello agregamos la siguiente validacion en nuestro metodo comer pepinos.
```py
def  comer(self, pepinos):
	if  pepinos  <  0:
		raise  ValueError("La cantidad de pepinos no puede ser negativo")
	self.pepinos_comidos  +=  pepinos
```
Planteamos el scenario en gherkin que verifica que se produzca un error al intentar comer una cantidad negativa de pepinos.
 <div align="center">
      <img src="https://i.postimg.cc/05S8PpBP/7-5.png" alt="Parte1" width="600" />
    </div>


#### Ejercicio 6: **Escalabilidad con grandes cantidades de pepinos**
Para ello agregamos la siguiente validacion en nuestro metodo comer pepinos.
```py
if  pepinos  >  1000:
	raise  ValueError("No se puede comer mas de 1000 pepinos")
```
Quedando asi nuestro metodo.
```py
def  comer(self, pepinos):
	if  pepinos  <  0:
		raise  ValueError("La cantidad de pepinos no puede ser negativo")
	if  pepinos  >  1000:
		raise  ValueError("No se puede comer mas de 1000 pepinos")
	self.pepinos_comidos  +=  pepinos
```
Ahora agreguemos un scenario en gherkin para validar esta nueva funcionalidad.
  <div align="center">
      <img src="https://i.postimg.cc/DzmTDsGV/7-6.png" alt="Parte1" width="600" />
    </div>


#### Ejercicio 7: **Descripciones de tiempo complejas**
Para esto es necesario modificar nuestro regex para que busque todas las coincidencias independientemente del orden por ello es necesario usar re.findall y buscar las tuplas con su respectivo valor y unidad de tiempo. 
```py
pattern  =  re.findall(r'(\w+(?:\.\d+)?)\s*(horas?|hours?|minutos?|minutes?|segundos?|seconds?)', time_description)
```
Entonces, ahora nuestra funcion queda de esta forma.
```py
def  convertir_tiempo_a_horas(time_description):
	tiempo_random  =  generar_tiempo_aleatorio(time_description)
	if  tiempo_random  is  not  None:
	return  tiempo_random

	time_description  =  time_description.strip('"').lower()
	time_description  =  time_description.replace(",", " ")
	time_description  =  time_description.replace(" y ", " ")
	time_description  =  time_description.replace(" and ", " ")
	time_description  =  time_description.strip()

	if  time_description  in ['media hora', 'half an hour']:
	return  0.5

	pattern  =  re.findall(r'(\w+(?:\.\d+)?)\s*(horas?|hours?|minutos?|minutes?|segundos?|seconds?)', time_description)
	total_time_in_hours  =  0.0
	for  cantidad, unidad  in  pattern:
		try:
			valor  =  convertir_palabra_a_numero(cantidad)
		except  ValueError  as  e:
			raise  ValueError(f"Error al interpretar la cantidad: {e}")
			
		if  "hora"  in  unidad  or  "hour"  in  unidad:
			total_time_in_hours  +=  valor
		elif  "minuto"  in  unidad  or  "minute"  in  unidad:
			total_time_in_hours  +=  valor  /  60
		elif  "segundo"  in  unidad  or  "second"  in  unidad:
			total_time_in_hours  +=  valor  /  3600
		else:
			raise  ValueError(f"Unidad no reconocida: {unidad}")
	return  round(total_time_in_hours, 4)
```
Ahora creamos dos scenarios, uno en ingles y otro en español para verificar que se manejan descripciones de tiempo complejas.
<div align="center">
      <img src="https://i.postimg.cc/1tqZRQMJ/7-7.png" alt="Parte1" width="600" />
    </div>

#### Ejercicio 8: **De TDD a BDD – Convertir requisitos técnicos a pruebas en Gherkin**
Implementaremos la siguiente prueba unitaria.
```py
def  test_estomago_gruñir_si_comido_muchos_pepinos():
	belly  =  Belly()
	belly.comer(15)
	belly.esperar(2)
	assert  belly.esta_gruñendo() ==  True
```
Ahora pasaremos esta prueba unitaria a un scenario de gherkin.
 <div align="center">
      <img src="https://i.postimg.cc/jdb2FwW5/d-8-2.png" alt="Parte1" width="600" />
    </div>
Ahora verificamos que el test pase exitosamente.
 <div align="center">
      <img src="https://i.postimg.cc/gjbbnTTd/7-8.png" alt="Parte1" width="600" />
    </div>

#### Ejercicio 9: **Identificación de criterios de aceptación para historias de usuario**
**Usando** la siguiente historia de usuario:  
   > "Como usuario que ha comido pepinos, quiero saber si mi estómago va a gruñir después de esperar un tiempo suficiente, para poder tomar una acción."
 
 Para ello recordemos que el estomago gruñe cuando el usuario come mas de 10 pepinos y espera mas de 1.5 horas en caso contrario no debe gruñir.
 Entonces planteamos los siguientes escenarios.
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
Refactorizamos nuestra funcion esta_gruñendo() de la siguiente manera.
```python
def  esta_gruñendo(self):
	return  self.tiempo_esperado  >=  1.5  and  self.pepinos_comidos  >  10
```
Luego agregamos un test para verificar casos en los que el estomago no gruñe sino se espera lo suficiente.

```python
def  test_estomago_no_gruñe_si_no_espera_suficiente():
	belly  =  Belly()
	belly.comer(20)
	belly.esperar(1)
	assert  belly.esta_gruñendo() ==  False
```
   <div align="center">
      <img src="https://i.postimg.cc/LsGrbWRf/7-11.png" alt="Parte1" width="600" />
    </div>


#### Ejercicio 12: **Ciclo completo de TDD a BDD – Añadir nueva funcionalidad**
Nos plantearemos el caso en el que queremos predecir si el estomago gruñira, si es que comieramos una determinada cantidad de pepinos y esperaramos cierto tiempo. Para ello agregamos la funcion `predecir_gruñido`.
```python
def  predecir_gruñido(self, pepinos, tiempo_en_horas):
	return  pepinos  >  10  and  tiempo_en_horas  >=  1.5
```
Procedemos a realizar el `test_predecir_gruñido()`en el cual evaluamos dos casos
en el cual debe predecir que gruñira y en el otro que no.
```py
def  test_predecir_gruñido():
	belly  =  Belly()
	assert  belly.predecir_gruñido(12, 2) ==  True
	assert  belly.predecir_gruñido(12, 1) ==  False
```
Ahora planteamos los escenarios en gherkin y verificamos que sean exitosos
al igual que los test.
<div align="center">
      <img src="https://i.postimg.cc/Ss8wFGNP/7-12.png" alt="Parte1" width="600" />
    </div>
    <div align="center">
      <img src="https://i.postimg.cc/1Xr245Fc/7-12-1.png" alt="Parte1" width="600" />
    </div>

#### Ejercicio 13: **Añadir criterios de aceptación claros**
**Definir** una nueva historia de usuario. 
   > "Como usuario que ha comido pepinos, quiero saber cuantos pepinos mas puedo comer antes que mi estómago gruña, para poder tomar una acción."
  
Podemos formular lo siguientes criterios de aceptación.
- Si el usuario a comido 8 pepinos, se le debe decir que puede comer 2 pepinos mas.
- Si el usuario a comido 10 pepinos, se le debe decir que puede comer 0 pepinos mas.
 <div align="center">
      <img src="https://i.postimg.cc/qMQWTq4p/7-13.png" alt="Parte1" width="600" />
    </div>

#### Ejercicio 14: **Integración con Mocking, Stubs y Fakes (para DevOps)**
Modificamos belly() para que acepte un clock_service  
```py
def  __init__(self,clock_service=None):
	self.pepinos_comidos  =  0
	self.tiempo_esperado  =  0
	self.clock  =  clock_service  or (lambda: None)
```
Ahora modificamos nuestro before_scenario para que use un mock en cada contexto y  evitar fallos con la hora en tiempo real del sistema.
```py
def before_scenario(context, scenario):
    clock_simulado = Mock()
    clock_simulado.return_value = "2025-02-22 12:00" 
    context.belly = Belly(clock_service=clock_simulado)
    context.fake_clock = clock_simulado  
```
Finalmente creamos un scenario con gherkin para validar dicha implementacion.
 <div align="center">
      <img src="https://i.postimg.cc/MGfLVYRG/7-14.png" alt="Parte1" width="600" />
    </div>

#### Ejercicio 15: **Despliegue y validación continua en un entorno de integración (CI/CD)**
**Configura** un pipeline en GitHub Actions con estos pasos:
   - Instalar dependencias (Python, Behave, Pytest).
   - Ejecutar pruebas unitarias (Pytest).
   - Ejecutar pruebas de comportamiento (Behave).
```yml
name: CI Belly
on:
  push:
    branches: [main]
    paths:
      - 'Actividad7/**'
  pull_request:
    branches: [main]
    paths:
      - 'Actividad7/**'

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest behave 
          pip install -r Actividad7/requirements.txt || true

  tests_unitarios:
    runs-on: ubuntu-latest
    needs: build

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Ejecutar pruebas unitarias con pytest
        run: |
          echo "Ejecutando pruebas unitarias..."
          pytest Actividad7/test/

  tests_bdd:
    runs-on: ubuntu-latest
    needs: build

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Ejecutar pruebas BDD
        run: |
          echo "Ejecutando pruebas BDD con behave..."
          behave Actividad7/features/ --no-capture --no-capture-stderr

```



