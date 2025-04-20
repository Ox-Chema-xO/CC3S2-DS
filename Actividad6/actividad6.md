## **Actividad 6: Rebase, Cherry-Pick y CI/CD en un entorno ágil**

### Objetivo de aprendizaje:  

Aprender a usar los comandos `git rebase` y `git cherry-pick` para mantener un historial de commits limpio y manejable en proyectos colaborativos.  También explorarás cuándo y por qué utilizar estos comandos en lugar de los merges regulares.

#### **Parte 1: git rebase para mantener un historial lineal**

1. **Introducción a Rebase:**

   El rebase mueve tus commits a una nueva base, dándote un historial lineal y limpio. En lugar de fusionar ramas y mostrar un "commit de merge", el rebase integra los cambios aplicándolos en la parte superior de otra rama.

   - **Caso de uso**: Simplifica la depuración y facilita la comprensión del historial de commits.

2. **Escenario de ejemplo:**

   - Crea un nuevo repositorio Git y dos ramas, main y new-feature:
   
   - Crea y cambia a la rama new-feature:

   - Presenta el historial de ramas obtenida hasta el momento.
 
   <div align="center">
      <img src="https://i.postimg.cc/sgqk4qHF/6-1.png" alt="Parte1-1" width="600" />
   </div>
   		
   Ahora, digamos que se han agregado nuevos commits a main mientras trabajabas en new-feature:
Tu gráfico de commits ahora diverge (comprueba esto)

   <div align="center">
      <img src="https://i.postimg.cc/XYjfDYhd/6-2.png" alt="Parte1-2" width="600" />
   </div>

   > **Tarea**: Realiza el rebase de `new-feature` sobre `main` con los siguientes comandos:
   ```bash
   $ git checkout new-feature
   $ git rebase main
   ```
    <div align="center">
      <img src="https://i.postimg.cc/NFNssbsg/6-3.png" alt="Parte1-3" width="600" />
   </div>
   

3. **Revisión:**

   Después de realizar el rebase, visualiza el historial de commits con:
   ```bash
   $ git log --graph –-oneline --all
   ```
   <div align="center">
      <img src="https://i.postimg.cc/pr1vbTCr/6-4.png" alt="Parte1-4" width="600" />
   </div>

   
4. **Momento de fusionar y completar el proceso de git rebase:**
   ```bash
   # Cambiar a 'main' y realizar una fusión fast-forward
   $ git checkout main
   $ git merge new-feature
   ```
   <div align="center">
      <img src="https://i.postimg.cc/W3gScf7k/6-5.png" alt="Parte1-5" width="600" />
  </div>
   Cuando se realiza una fusión *fast-forward*, las HEADs de las ramas main y new-feature serán los commits correspondientes.                                                                                        					      <div align="center">
      <img src="https://i.postimg.cc/fbvdKWJP/6-6.png" alt="Parte1-6" width="600" />
</div>
       
#### Parte 2: **git cherry-pick para la integración selectiva de commit**
1. **Introducción a Cherry-pick:**

   `git cherry-pick` te permite seleccionar commits individuales de una rama y aplicarlos en otra. Esto es útil cuando necesitas integrar una característica o corrección sin hacer merge de toda la rama.

   Imagina que tienes dos ramas, main y feature. Te das cuenta de que uno o dos commits de la rama feature deberían moverse a main, pero no estás listo para fusionar toda la rama. El comando `git cherry-pick` te permite hacer precisamente eso.

   Puedes hacer cherry-pick de los cambios de un commit específico en la rama feature y aplicarlos en la rama main.
   Esta acción creará un nuevo commit en la rama main.


2. **Escenario de ejemplo:**
 - Inicializar un nuevo repositorio
 - Agregar y commitear README inicial a main
 - Crear y cambiar a una nueva rama 'add-base-documents'
 - Hacer cambios y commitearlos
	 - Agregar CONTRIBUTING
	 - Agregar LICENSE.txt
- Echa un vistazo al log de la rama 'add-base-documents'

   <div align="center">
      <img src="https://i.postimg.cc/L85CZ75L/6-7.png" alt="Parte2-1" width="600" />
   </div>

3. **Tarea: Haz cherry-pick de un commit de add-base-documents a main.**
4. **Revisión: Revisa el historial nuevamente.**  
   
   <div align="center">
      <img src="https://i.postimg.cc/MZYd3xj1/6-8.png" alt="Parte2-2" width="600" />
   </div>


##### **Preguntas de discusión:**

1. ¿Por qué se considera que rebase es más útil para mantener un historial de proyecto lineal en comparación con merge?  
	 - Debido a que mantiene un historial limpio y no muestra “commit de merge” facilitando la comprensión del historial de commits.
2. ¿Qué problemas potenciales podrían surgir si haces rebase en una rama compartida con otros miembros del equipo?  
	- Se puede sobrescribir el historial remoto y borrar el trabajo(commits) de otro miembro del equipo en dicha rama ya que el rebase cambia hashes y causa divergencia del historial.
3. ¿En qué se diferencia cherry-pick de merge, y en qué situaciones preferirías uno sobre el otro?  
	 - Merge fusiona la rama completa en cambio cherry-pick permite seleccionar commits individuales de una rama y aplicarlos en otra. Entonces cuando solo quiera traer cierto commits a una rama, usare cherry-pick, en cambio si quiero traer todos los commits de una rama usare merge.
4. ¿Por qué es importante evitar hacer rebase en ramas públicas?
	- Es importante ya que dicha rama es compartida por otros miembros del equipo y al hacer rebase se puede generar conflictos complejos de resolver ya que sus versiones quedarán desactualizadas y en otros casos se puede llegar a perder el trabajo de otro integrante.

 #### **Ejercicios teóricos**

1. **Diferencias entre git merge y git rebase**  
   **Pregunta**: Explica la diferencia entre git merge y git rebase y describe en qué escenarios sería más adecuado utilizar cada uno en un equipo de desarrollo ágil que sigue las prácticas de Scrum.
	 - `git merge` fusiona ramas y conserva la historia completa de cómo divergen y se fusionan, incluyendo commits de merge. En cambio, `git rebase` reescribe el historial al mover los commits de una rama sobre otra, creando un historial más lineal y limpio.
	- En un equipo Scrum, `merge` es útil cuando se quiere preservar el contexto de la integración entre ramas, por ejemplo, al integrar una `feature/login` a `develop`. En cambio, `rebase` es ideal para mantener un historial limpio durante el trabajo local o en ramas pequeñas antes de integrarlas, ayudando a hacer revisiones más claras en pull requests.

2. **Relación entre git rebase y DevOps**  
   **Pregunta**: ¿Cómo crees que el uso de git rebase ayuda a mejorar las prácticas de DevOps, especialmente en la implementación continua (CI/CD)? Discute los beneficios de mantener un historial lineal en el contexto de una entrega continua de código y la automatización de pipelines.
	-	Usar `git rebase` permite que los cambios se integren sin commits de merge innecesarios, lo que facilita automatizar pruebas, analizar cambios y hacer despliegues controlados. Esto es clave para la entrega continua, donde cada cambio debe ser claro, probado y desplegado sin ambigüedad, reduciendo errores en pipelines de CI/CD, siguiendo prácticas de `DevOps`.

3. **Impacto del git cherry-pick en un equipo Scrum**  
   **Pregunta**: Un equipo Scrum ha finalizado un sprint, pero durante la integración final a la rama principal (main) descubren que solo algunos commits específicos de la rama de una funcionalidad deben aplicarse a producción. ¿Cómo podría ayudar git cherry-pick en este caso? Explica los beneficios y posibles complicaciones.
   - Si solo algunos commits de una funcionalidad deben ir a producción, `git cherry-pick` permite traerlos a `main` sin fusionar toda la rama. Esto permite controlar exactamente qué cambios se estan aplicando.
	- Los beneficios son que evita traer código incompleto, innecesario o no testeado; permite hotfixes o entregas parciales. Sin embargo, puede haber conflictos si los commits que decidimos integrar dependen de otros cambios no seleccionados o si ya hubo modificaciones similares en `main`.

#### **Ejercicios prácticos**

1. **Simulación de un flujo de trabajo Scrum con git rebase y git merge**

   **Contexto:**  
   Tienes una rama `main` y una rama `feature` en la que trabajas. Durante el desarrollo del sprint, se han realizado commits tanto en `main` como en `feature`.  

   Tu objetivo es integrar los cambios de la rama `feature` en `main` manteniendo un historial limpio.

   **Instrucciones:**

   - Crea un repositorio y haz algunos commits en la rama main.
   - Crea una rama feature, agrega nuevos commits, y luego realiza algunos commits adicionales en main.
   - Realiza un rebase de feature sobre main.
   - Finalmente, realiza una fusión fast-forward de feature con main.
    <div align="center">
      <img src="https://i.postimg.cc/TY8wHyB4/6-9.png" alt="Parte2-3" width="600" />
   </div>

   **Preguntas:**

   - ¿Qué sucede con el historial de commits después del rebase?  
	   - Se reescribe el historial de la rama `feature`, colocando sus commits después de los commits de `main`. El historial resultante es lineal, sin commits de merge, facilitando la lectura, depuración y revisión de cambios. 
   - ¿En qué situación aplicarías una fusión fast-forward en un proyecto ágil?
	   - Cuando el equipo no hizo cambios nuevos en main desde que se creo la rama `feature` o cuando el equipo ya hizo `rebase` de la rama `feature` sobre `main`, y no hay commits nuevos en `main` desde entonces, para mantener un historial de proyecto lineal, lo que simplifica la depuración y facilita las revisiones del código

2. **Cherry-pick para integración selectiva en un pipeline CI/CD**

   **Contexto:**  
   Durante el desarrollo de una funcionalidad, te das cuenta de que solo ciertos cambios deben ser integrados en la rama de producción, ya que el resto aún está en desarrollo. Para evitar fusionar toda la rama, decides hacer cherry-pick de los commits que ya están listos para producción.

   **Instrucciones:**

   - Crea un repositorio con una rama main y una rama feature.
   - Haz varios commits en la rama feature, pero solo selecciona uno o dos commits específicos que consideres listos para producción.
   - Realiza un cherry-pick de esos commits desde feature a main.
   - Verifica que los commits cherry-picked aparezcan en main.
   <div align="center">
      <img src="https://i.postimg.cc/pThWsxCv/6-10.png" alt="Parte2-4" width="600" />
   </div>

   **Preguntas:**

   - ¿Cómo utilizarías cherry-pick en un pipeline de CI/CD para mover solo ciertos cambios listos a producción?  
	   - Cuando algunas partes del código en una rama de desarrollo no están listas para producción, uso `git cherry-pick` para mover solo los commits que sí lo están a la rama `main` para pasasr las pruebas y desplegarse. Esto permite avanzar en producción sin tener que hacer merge de toda la rama, evitando que se despliegue código incompleto o cambios que aún no están listos para pasar a producción
   - ¿Qué ventajas ofrece cherry-pick en un flujo de trabajo de DevOps?
	   -  Permite **Integración selectiva** sobre qué cambios se integran a producción, sin romper el resto del desarrollo. Además, **reversión fácil**   e **historial limpio**. Esto lo convierte en una herramienta invaluable para cualquier ingeniero DevOps que busque un flujo de trabajo de control de versiones flexible y eficiente.

#### **Git, Scrum y Sprints**

#### **Fase 1: Planificación del sprint (sprint planning)**
**Ejercicio 1: Crear ramas de funcionalidades (feature branches)**

En esta fase del sprint, los equipos Scrum deciden qué historias de usuario van a trabajar. Cada historia de usuario puede representarse como una rama de funcionalidad.

**Objetivo:** Crear ramas para cada historia de usuario y asegurar que el trabajo se mantenga aislado.

**Instrucciones:**

1. Crea un repositorio en Git.
2. Crea una rama `main` donde estará el código base.
3. Crea una rama por cada historia de usuario asignada al sprint, partiendo de la rama `main`.
   <div align="center">
      <img src="https://i.postimg.cc/T3Sx4F4J/6-11.png" alt="Parte3-1" width="600" />
   </div>

**Pregunta:** ¿Por qué es importante trabajar en ramas de funcionalidades separadas durante un sprint?
- Porque permite que cada desarrollador trabaje de forma aislada, sin afectar directamente el código base (`main`) ni a otras funcionalidades.  
Además, facilita el control de versiones, las revisiones de código (pull requests) y evita conflictos innecesarios. También es clave para seguir buenas prácticas DevOps en equipos Scrum y mantener el repositorio limpio y bien organizado.


#### **Fase 2: Desarrollo del sprint (sprint execution)**

**Ejercicio 2: Integración continua con git rebase**

A medida que los desarrolladores trabajan en sus respectivas historias de usuario, pueden ocurrir cambios en main. Para mantener un historial lineal y evitar conflictos más adelante, se usa `git rebase` para integrar los últimos cambios de main en las ramas de funcionalidad antes de finalizar el sprint.

**Objetivo:** Mantener el código de la rama de funcionalidad actualizado con los últimos cambios de main durante el sprint.

**Instrucciones:**

1. Haz algunos commits en main.
2. Realiza un rebase de la rama `feature-user-story-1` para actualizar su base con los últimos cambios de main.
   <div align="center">
      <img src="https://i.postimg.cc/KYMbSQXS/6-12.png" alt="Parte3-2" width="600" />
   </div>


**Pregunta:** ¿Qué ventajas proporciona el rebase durante el desarrollo de un sprint en términos de integración continua?
- Permite mantener las ramas de funcionalidades actualizadas con los últimos cambios de main sin commits de merge innecesarios.
- Eso ayuda a que cuando llegue el momento de integrar todo al final del sprint, el proceso sea más limpio y sin conflictos. También mejora la automatización en pipelines CI/CD, ya que un historial lineal es más fácil de analizar por scripts o herramientas de despliegue continuo.

#### **Fase 3: Revisión del sprint (sprint review)**

**Ejercicio 3: Integración selectiva con git cherry-pick**

En esta fase, es posible que algunas funcionalidades estén listas para ser mostradas a los stakeholders, pero otras aún no están completamente implementadas. Usar `git cherry-pick` puede permitirte seleccionar commits específicos para mostrar las funcionalidades listas, sin hacer merge de ramas incompletas.

**Objetivo:** Mover commits seleccionados de una rama de funcionalidad (`feature-user-story-2`) a `main` sin integrar todos los cambios.

**Instrucciones:**

1. Realiza algunos commits en `feature-user-story-2`.
2. Haz cherry-pick de los commits que estén listos para mostrarse a los stakeholders durante la revisión del sprint.
   <div align="center">
      <img src="https://i.postimg.cc/1t0Z4t5v/6-13.png" alt="Parte3-3" width="600" />
   </div>

**Pregunta:** ¿Cómo ayuda `git cherry-pick` a mostrar avances de forma selectiva en un sprint review?
- Permite llevar solo los commits que están completos a `main` sin tener que fusionar ramas enteras que tienen partes en desarrollo.
- Esto es útil para la revisión del sprint, ya que el equipo puede mostrar avances funcionales sin comprometer estabilidad ni fusionar código incompleto. También facilita que el equipo de QA o los stakeholders prueben algo funcional, mientras el resto del trabajo sigue aún en progreso.

#### **Fase 4: Retrospectiva del sprint (sprint retrospective)**

**Ejercicio 4: Revisión de conflictos y resolución**

Durante un sprint, pueden surgir conflictos al intentar integrar diferentes ramas de funcionalidades. Es importante aprender cómo resolver estos conflictos y discutirlos en la retrospectiva.

**Objetivo:** Identificar y resolver conflictos de fusión con `git merge` al intentar integrar varias ramas de funcionalidades al final del sprint.

**Instrucciones:**

1. Realiza cambios en `feature-user-story-1` y `feature-user-story-2` que resulten en conflictos.
2. Intenta hacer merge de ambas ramas con main y resuelve los conflictos.
   <div align="center">
      <img src="https://i.postimg.cc/t41QWD4Z/6-14.png" alt="Parte3-4" width="600" />
   </div>
   <div align="center">
      <img src="https://i.postimg.cc/85S28SBM/6-15.png" alt="Parte3-5" width="600" />
   </div>
      <div align="center">
      <img src="https://i.postimg.cc/ydywsbv5/6-16.png" alt="Parte3-6" width="600" />
   </div>

**Pregunta**: ¿Cómo manejas los conflictos de fusión al final de un sprint? ¿Cómo puede el equipo mejorar la comunicación para evitar conflictos grandes?
- Para resolver conflictos al final del sprint se requiere entender bien el propósito de cada cambio para decidir qué conservar. Por eso, es clave la comunicación continua con el equipo para tener el contexto de cada cambio.
- Para evitarlos, cada integrante del equipo puede comunicar claramente qué parte del código modifica para evitar tocar las mismas líneas entre features y estar en constante comunicacion para mantener un historial limpio que mantegan la trazabilidad y ayude a preever posibles conflictos.
    
#### **Fase 5: Fase de desarrollo, automatización de integración continua (CI) con git rebase**

**Ejercicio 5: Automatización de rebase con hooks de Git**

En un entorno CI, es común automatizar ciertas operaciones de Git para asegurar que el código se mantenga limpio antes de que pase a la siguiente fase del pipeline. Usa los hooks de Git para automatizar el rebase cada vez que se haga un push a una rama de funcionalidad.

**Objetivo:** Implementar un hook que haga automáticamente un rebase de `main` antes de hacer push en una rama de funcionalidad, asegurando que el historial se mantenga limpio.

**Instrucciones:**

1. Configura un hook `pre-push` que haga un rebase automático de la rama `main` sobre la rama de funcionalidad antes de que el push sea exitoso.
**Comandos:**
	```bash
	# Dentro de tu proyecto, crea un hook pre-push
	$ nano .git/hooks/pre-push

	# Agrega el siguiente script para automatizar el rebase
	#!/bin/bash
	git fetch origin main
	git rebase origin/main

	# Haz el archivo ejecutable
	$ chmod +x .git/hooks/pre-push
	```
2. Prueba el hook haciendo push de algunos cambios en la rama `feature-user-story-1`.
   <div align="center">
      <img src="https://i.postimg.cc/Y02T9zPS/6-17.png" alt="Parte3-7" width="600" />
   </div>

**Pregunta**: ¿Qué ventajas y desventajas observas al automatizar el rebase en un entorno de CI/CD?
- **Ventajas:**
	- Historial lineal:  Es más fácil de entender que el historial no lineal creado por  `git merge`, lo cual facilita los merges a producción.
	- Depuración simplificada: Rastrear cuándo se introdujo un error en particular se vuelve más fácil.
	- Higiene del código: El rebasing te anima a aplastar commits de corrección o dividir commits más grandes, reduce conflictos posteriores porque siempre trabajas con lo más actualizado de `main`.
	
- **Desventajas:**
	- Conflictos para los colaboradores sino están familiarizados.
	- Fusiones complejas en caso una rama pública ha sido rebased y se ha alterado el historial.
	- Pérdida de contexto al aplatas commits.
---

### **Navegando conflictos y versionado en un entorno devOps**
**Objetivo:**  
Gestionar conflictos en Git, realizar fusiones complejas, utilizar herramientas para comparar y resolver conflictos, aplicar buenas prácticas en el manejo del historial de versiones  y usar el versionado semántico en un entorno de integración continua (CI).
#### **Ejemplo:**

1. **Inicialización del proyecto y creación de ramas**

   - **Paso 1**: Crea un nuevo proyecto en tu máquina local.
     ```bash
     $ mkdir proyecto-colaborativo
     $ cd proyecto-colaborativo
     ```
   - **Paso 2**: Inicializa Git en tu proyecto.
     ```bash
     $ git init
     ```
   - **Paso 3**: Crea un archivo de texto llamado `archivo_colaborativo.txt` y agrega algún contenido inicial.
     ```bash
     $ echo "Este es el contenido inicial del proyecto" > archivo_colaborativo.txt
     ```
   - **Paso 4**: Agrega el archivo al área de staging y haz el primer commit.
     ```bash
     $ git add .
     $ git commit -m "Commit inicial con contenido base"
     ```
   - **Paso 5**: Crea dos ramas activas: main y feature-branch.
     ```bash
     $ git branch feature-branch  # Crear una nueva rama
     ```
   - **Paso 6**: Haz checkout a la rama feature-branch y realiza un cambio en el archivo `archivo_colaborativo.txt`.
     ```bash
     $ git checkout feature-branch
     $ echo "Este es un cambio en la feature-branch" >> archivo_colaborativo.txt
     $ git add .
     $ git commit -m "Cambios en feature-branch"
     ```
   - **Paso 7**: Regresa a la rama main y realiza otro cambio en la misma línea del archivo `archivo_colaborativo.txt`.
     ```bash
     $ git checkout main
     $ echo "Este es un cambio en la rama main" >> archivo_colaborativo.txt
     $ git add .
     $ git commit -m "Cambios en main"
     ```
   <div align="center">
      <img src="https://i.postimg.cc/mDm1Skpr/6-18.png" alt="Parte4-1" width="600" />
   </div>


2. **Fusión y resolución de conflictos**

   - **Paso 1**: Intenta fusionar feature-branch en main. Se espera que surjan conflictos de fusión.
     ```bash
     $ git merge feature-branch
     ```
   - **Paso 2**: Usa `git status` para identificar los archivos en conflicto. Examina los archivos afectados y resuelve manualmente los conflictos, conservando las líneas de código más relevantes para el proyecto.
     ```bash
     $ git status
     $ git checkout --theirs <archivo>  # Si decides aceptar los cambios de feature-branch
     $ git checkout --ours <archivo>    # Si decides aceptar los cambios de main
     ```
   - **Paso 3**: Una vez resueltos los conflictos, commitea los archivos y termina la fusión
     ```bash
     $ git add .
     $ git commit -m "Conflictos resueltos"
     ```
   <div align="center">
      <img src="https://i.postimg.cc/brMGKMhc/6-19.png" alt="Parte4-2" width="600" />
   </div>
3. **Simulación de fusiones y uso de git diff**

   - **Paso 1**: Simula una fusión usando `git merge --no-commit --no-ff` para ver cómo se comportarían los cambios antes de realizar el commit.
     ```bash
     $ git merge --no-commit --no-ff feature-branch
     $ git diff --cached  # Ver los cambios en el área de staging
     $ git merge --abort  # Abortar la fusión si no es lo que se esperaba
     ```
   <div align="center">
      <img src="https://i.postimg.cc/d373mBTW/6-20.png" alt="Parte4-3" width="600" />
   </div>
4. **Uso de git mergetool**

   - **Paso 1**: Configura git mergetool con una herramienta de fusión visual (puedes usar meld, vimdiff, o Visual Studio Code).
     ```bash
     $ git config --global merge.tool <nombre-herramienta>
     $ git mergetool
     ```
   - **Paso 2**: Usa la herramienta gráfica para resolver un conflicto de fusión.
    <div align="center">
      <img src="https://i.postimg.cc/tCWPKqYB/6-21.png" alt="Parte4-4" width="600" />
   </div>

      <div align="center">
      <img src="https://i.postimg.cc/Cx48KcCD/6-22.png" alt="Parte4-5" width="600" />
   </div>
   
      <div align="center">
      <img src="https://i.postimg.cc/hGy7Lh5t/6-23.png" alt="Parte4-5" width="600" />
   </div>
5. **Uso de git revert y git reset**

   - **Paso 1**: Simula la necesidad de revertir un commit en main debido a un error. Usa `git revert` para crear un commit que deshaga los cambios.
     ```bash
     $ git revert <commit_hash>
     ```
    <div align="center">
      <img src="https://i.postimg.cc/Y9TGPZkc/6-24.png" alt="Parte4-6" width="600" />
   </div>

   - **Paso 2**: Realiza una prueba con `git reset --mixed` para entender cómo reestructurar el historial de commits sin perder los cambios no commiteados.
     ```bash
     $ git reset --mixed <commit_hash>
     ```
    <div align="center">
      <img src="https://i.postimg.cc/3rDDG8C3/6-25.png" alt="Parte4-7" width="600" />
   </div>
   <div align="center">
       <img src="https://i.postimg.cc/Vk4Swd1W/6-26.png" alt="Parte4-8" width="600" />
    </div>

6. **Versionado semántico y etiquetado**

   - **Paso 1**: Aplica versionado semántico al proyecto utilizando tags para marcar versiones importantes.
     ```bash
     $ git tag -a v1.0.0 -m "Primera versión estable"
     $ git push origin v1.0.0
     ```
         <div align="center">
       <img src="https://i.postimg.cc/6p63MtR2/6-27.png" alt="Parte4-9" width="600" />
    </div>

7. **Aplicación de git bisect para depuración**

   - **Paso 1**: Usa `git bisect` para identificar el commit que introdujo un error en el código.
     ```bash
     $ git bisect start
     $ git bisect bad   # Indica que la versión actual tiene un error
     $ git bisect good <último_commit_bueno>
     # Continúa marcando como "good" o "bad" hasta encontrar el commit que introdujo el error
     $ git bisect reset  # Salir del modo bisect
     ```
  --   Creamos una función para sumar dos números con 4 fases
  <div align="center">
       <img src="https://i.postimg.cc/9FQ5SM8h/6-31.png" alt="Parte4-12" width="600" />
    </div>
          <div align="center">
       <img src="https://i.postimg.cc/V6PPHWTG/6-30.png" alt="Parte4-11" width="600" />
    </div>
     
-- Usamos `git bisect` para identificar el commit que introdujo el error 
   <div align="center">
       <img src="https://i.postimg.cc/MTqrQPgS/6-32.png" alt="Parte4-13" width="600" />
    </div>
    
 --  Corregimos el error
   <div align="center">
       <img src="https://i.postimg.cc/R0XwggN9/6-33.png" alt="Parte4-14" width="600" />
     </div>
    <div align="center">
       <img src="https://i.postimg.cc/sxZSDyKD/6-34.png" alt="Parte4-14" width="600" />
     </div>

---
#### **Preguntas**

1. **Ejercicio para git checkout --ours y git checkout --theirs**

   **Contexto**: En un sprint ágil, dos equipos están trabajando en diferentes ramas. Se produce un conflicto de fusión en un archivo de configuración crucial. El equipo A quiere mantener sus cambios mientras el equipo B solo quiere conservar los suyos. El proceso de entrega continua está detenido debido a este conflicto.

   **Pregunta**:  
   ¿Cómo utilizarías los comandos `git checkout --ours` y `git checkout --theirs` para resolver este conflicto de manera rápida y eficiente? Explica cuándo preferirías usar cada uno de estos comandos y cómo impacta en el pipeline de CI/CD. ¿Cómo te asegurarías de que la resolución elegida no comprometa la calidad del código?
   
 - Ante todo, esto se soluciona con una comunicacion continua en equipo, por ello, usaría `git checkout --ours` si quiero priorizar los cambios de mi rama actual en la que estoy trabajando y los cambios de la otra rama aun no son funcionales o no fueron probados. En cambio, `git checkout --theirs` para traer los cambios de la rama que estoy fusionando sabiendo que son correctos o si ya fueron validados por el otro equipo, aparte resolver el conflicto permite que el pipeline continúe su ejecución lo más antes posible. 
 - Ejecutaria los tests del pipeline CI/CD para asegurarme de que la resolución elegida no comprometa la calidad del código y el flujo del pipeline se mantega estable. 

2. **Ejercicio para git diff**

   **Contexto**: Durante una revisión de código en un entorno ágil, se observa que un pull request tiene una gran cantidad de cambios, muchos de los cuales no están relacionados con la funcionalidad principal. Estos cambios podrían generar conflictos con otras ramas en la pipeline de CI/CD.

   **Pregunta**:  
   Utilizando el comando `git diff`, ¿cómo compararías los cambios entre ramas para identificar diferencias específicas en archivos críticos? Explica cómo podrías utilizar `git diff feature-branch..main` para detectar posibles conflictos antes de realizar una fusión y cómo esto contribuye a mantener la estabilidad en un entorno ágil con CI/CD.
   
 - Usando, por ejemplo, `git diff feature-branch..main`, que muestra una comparación línea por línea de los cambios entre `feature-branch` y `main`. Esto me permitiría detectar posibles conflictos antes de realizar la fusión y así evitar que se detenga el pipeline CI/CD de manera innecesaria por conflictos en la fusión que se pueden evitar.
 
3. **Ejercicio para git merge --no-commit --no-ff**

   **Contexto**: En un proyecto ágil con CI/CD, tu equipo quiere simular una fusión entre una rama de desarrollo y la rama principal para ver cómo se comporta el código sin comprometerlo inmediatamente en el repositorio. Esto es útil para identificar posibles problemas antes de completar la fusión.

   **Pregunta**:  
   Describe cómo usarías el comando `git merge --no-commit --no-ff` para simular una fusión en tu rama local. ¿Qué ventajas tiene esta práctica en un flujo de trabajo ágil con CI/CD, y cómo ayuda a minimizar errores antes de hacer commits definitivos? ¿Cómo automatizarías este paso dentro de una pipeline CI/CD?
   
  - Permite simular una fusión para ver qué sucederá, y esto es de gran ayuda, ya que nos evitaría conflictos y, en consecuencia, que se detenga el pipeline CI/CD. Para automatizar esto, crearía un job que realice esta fusión en un entorno aislado y ejecute pruebas, reportando los resultados sin alterar nuestro repositorio.

4. **Ejercicio para git mergetool**

   **Contexto**: Tu equipo de desarrollo utiliza herramientas gráficas para resolver conflictos de manera colaborativa. Algunos desarrolladores prefieren herramientas como vimdiff o Visual Studio Code. En medio de un sprint, varios archivos están en conflicto y los desarrolladores prefieren trabajar en un entorno visual para resolverlos.

   **Pregunta**:  
   Explica cómo configurarías y utilizarías `git mergetool` en tu equipo para integrar herramientas gráficas que faciliten la resolución de conflictos. ¿Qué impacto tiene el uso de `git mergetool` en un entorno de trabajo ágil con CI/CD, y cómo aseguras que todos los miembros del equipo mantengan consistencia en las resoluciones?

- Para configurar `git mergetool`, usaría `git config --global merge.tool <herramienta>` para definir la herramienta preferida, en mi caso, vscode.  
En CI/CD, `git mergetool` acelra la resolución de conflictos con interfaces visuales más sencillas de usar, reduciendo el tiempo de bloqueo en el pipeline.  
Para mantener consistencia, podemos acordar en usar una herramienta estándar para todo el equipo y documentar nuestro proceso para reducir los conflictos de fusión.

5. **Ejercicio para git reset**

   **Contexto**: En un proyecto ágil, un desarrollador ha hecho un commit que rompe la pipeline de CI/CD. Se debe revertir el commit, pero se necesita hacerlo de manera que se mantenga el código en el directorio de trabajo sin deshacer los cambios.

   **Pregunta**:  
   Explica las diferencias entre `git reset --soft`, `git reset --mixed` y `git reset --hard`. ¿En qué escenarios dentro de un flujo de trabajo ágil con CI/CD utilizarías cada uno? Describe un caso en el que usarías `git reset --mixed` para corregir un commit sin perder los cambios no commiteados y cómo afecta esto a la pipeline.
- `git reset --soft` deshace el commit, pero mantiene los cambios en el staging area (reorganizar commits).  
`git reset --mixed` deshace el commit y los cambios en el staging area, pero quedan en nuestro directorio de trabajo (corregir commits).  
`git reset --hard` elimina el commit y todos los cambios (situaciones críticas).  
Si un commit rompe la pipeline, usaría `git reset --mixed HEAD~1` para deshacer el commit, conservando mis cambios y corrigiendo el error para posteriormente realizar un commit.


6. **Ejercicio para git revert**

   **Contexto**: En un entorno de CI/CD, tu equipo ha desplegado una característica a producción, pero se ha detectado un bug crítico. La rama principal debe revertirse para restaurar la estabilidad, pero no puedes modificar el historial de commits debido a las políticas del equipo.

   **Pregunta**:  
   Explica cómo utilizarías `git revert` para deshacer los cambios sin modificar el historial de commits. ¿Cómo te aseguras de que esta acción no afecte la pipeline de CI/CD y permita una rápida recuperación del sistema? Proporciona un ejemplo detallado de cómo revertirías varios commits consecutivos.
-   Lo utilizaría de esta forma: `git revert <commit_hash>`, ya que es seguro usarlo en ramas compartidas debido a que no altera el historial, permitiéndome una eliminación limpia.
    
-   Para no afectar el CI/CD, me aseguraría de que todas las pruebas pasen exitosamente y comunicaría al equipo del revert. Para revertir múltiples commits consecutivos, usaría `git revert OLDEST_COMMIT^..NEWEST_COMMIT` y luego haría un único commit de reversión.
7. **Ejercicio para git stash**

   **Contexto**: En un entorno ágil, tu equipo está trabajando en una corrección de errores urgente mientras tienes cambios no guardados en tu directorio de trabajo que aún no están listos para ser committeados. Sin embargo, necesitas cambiar rápidamente a una rama de hotfix para trabajar en la corrección.

   **Pregunta**:  
   Explica cómo utilizarías `git stash` para guardar temporalmente tus cambios y volver a ellos después de haber terminado el hotfix. ¿Qué impacto tiene el uso de `git stash` en un flujo de trabajo ágil con CI/CD cuando trabajas en múltiples tareas? ¿Cómo podrías automatizar el proceso de *stashing* dentro de una pipeline CI/CD?
- Para guardar mis cambios temporalmente, usaría `git stash save "descripción"`, luego cambiaría a la rama del hotfix con `git checkout hotfix`, y al terminar, volvería a mi rama de trabajo y recuperaría mis cambios con `git stash apply`.
Para automatizar el proceso en CI/CD, crearía un script que detecte cambios locales antes de cambiar de rama y aplique stash automáticamente, guardando las referencias para recuperarlos después.

8. **Ejercicio para .gitignore**

   **Contexto**: Tu equipo de desarrollo ágil está trabajando en varios entornos locales con configuraciones diferentes (archivos de logs, configuraciones personales). Estos archivos no deberían ser parte del control de versiones para evitar confusiones en la pipeline de CI/CD.

   **Pregunta**:  
   Diseña un archivo `.gitignore` que excluya archivos innecesarios en un entorno ágil de desarrollo. Explica por qué es importante mantener este archivo actualizado en un equipo colaborativo que utiliza CI/CD y cómo afecta la calidad y limpieza del código compartido en el repositorio.
  

```
# Archivos de editor de código
.vscode/
.idea/

# Ignorar todos los archivos de log
*.log

# Ignorar archivos de configuración personal,local
config/personal/
.env
*.env

# Archivos de dependecias de Python
__pycache__/
*.pyc

```
Mantener actualizado el .gitignore es crucial porque evita que archivos irrelevantes saturen el repositorio, evita exponer datos sensibles, y previene conflictos innecesarios en CI/CD.

---

#### **Ejercicios adicionales**
##### **Ejercicio 1: Resolución de conflictos en un entorno ágil**

**Contexto:**  
Estás trabajando en un proyecto ágil donde múltiples desarrolladores están enviando cambios a la rama principal cada día. Durante una integración continua, se detectan conflictos de fusión entre las ramas de dos equipos que están trabajando en dos funcionalidades críticas. Ambos equipos han modificado el mismo archivo de configuración del proyecto.

**Pregunta:**  
- ¿Cómo gestionarías la resolución de este conflicto de manera eficiente utilizando Git y manteniendo la entrega continua sin interrupciones? ¿Qué pasos seguirías para minimizar el impacto en la CI/CD y asegurar que el código final sea estable?
-Usamos `git status` para detectar qué archivos están en conflicto y consultar a los desarrolladores de cada rama cuál fue el motivo de cada cambio, para solucionar los conflictos de la mejor forma posible y fusionar las ramas.  
Para minimizar el impacto en CI/CD, debemos crear una rama `fix-merge` en la cual solucionemos el problema y luego integrarla a la rama principal, evitando así detener el pipeline CI/CD y asegurando que el código final sea estable.

##### **Ejercicio 2: Rebase vs. Merge en integraciones ágiles**

**Contexto:**  
En tu equipo de desarrollo ágil, cada sprint incluye la integración de varias ramas de características. Algunos miembros del equipo prefieren realizar merge para mantener el historial completo de commits, mientras que otros prefieren rebase para mantener un historial lineal.

**Pregunta:**  
- ¿Qué ventajas y desventajas presenta cada enfoque (merge vs. rebase) en el contexto de la metodología ágil? ¿Cómo impacta esto en la revisión de código, CI/CD, y en la identificación rápida de errores?
- Usar `git merge` permite mantener todo el historial de commits y ver claramente cuándo se integró cada rama. Es más seguro porque no reescribe el historial y ayuda a entender el contexto de cada integración. En cambio, `git rebase` reordena los commits para crear un historial más limpio y lineal, lo cual facilita revisar el código sin los commits de merge sin embargo hacerlo en una rama compartida puede traer conflictos complejos de resolver. En CI/CD con `merge` tenemos mayor trazabilidad para dectectar el error por integracion en cambio con `rebase` tenemos un historial limpio, fácil de revisar y detectar errores.

##### **Ejercicio 3: Git Hooks en un flujo de trabajo CI/CD ágil**

**Contexto:**  
Tu equipo está utilizando Git y una pipeline de CI/CD que incluye tests unitarios, integración continua y despliegues automatizados. Sin embargo, algunos desarrolladores accidentalmente comiten código que no pasa los tests locales o no sigue las convenciones de estilo definidas por el equipo.

**Pregunta:**  
- Diseña un conjunto de Git Hooks que ayudaría a mitigar estos problemas, integrando validaciones de estilo y tests automáticos antes de permitir los commits. Explica qué tipo de validaciones implementarías y cómo se relaciona esto con la calidad del código y la entrega continua en un entorno ágil.

 Hook pre-commit
```bash
#!/bin/bash
echo " Verificando estilo de código"

# Verificar formato con black
if ! black . --check; then
    echo "El código no está formateado correctamente. Usa 'black .' para corregir."
    exit 1
fi

# Verificar estilo con flake8
if ! flake8 .; then
    echo "Se encontraron errores de estilo con flake8."
    exit 1
fi

echo "Estilo correcto - Commit"
```

Hook pre-push
```bash
#!/bin/bash

echo "Ejecutando tests antes del push"

# Ejecutar pytest
if ! pytest; then
    echo "Los tests fallaron - Push cancelado"
    exit 1
fi

echo "Los tests pasaron exitosamente - Push"
```
En un entorno ágil con CI/CD, esto es clave para sostener un flujo constante de entregas pequeñas, limpias y funcionales.


##### **Ejercicio 4: Estrategias de branching en metodologías ágiles**

**Contexto:**  
Tu equipo de desarrollo sigue una metodología ágil y está utilizando Git Flow para gestionar el ciclo de vida de las ramas. Sin embargo, a medida que el equipo ha crecido, la gestión de las ramas se ha vuelto más compleja, lo que ha provocado retrasos en la integración y conflictos de fusión frecuentes.

**Pregunta:**  
- Explica cómo adaptarías o modificarías la estrategia de branching para optimizar el flujo de trabajo del equipo en un entorno ágil y con integración continua. Considera cómo podrías integrar feature branches, release branches y hotfix branches de manera que apoyen la entrega continua y minimicen conflictos.
- Para optimizar el flujo en un entorno ágil con CI/CD, en Git Flow eliminaria ramas de release si no son necesarias y manteniendo ramas cortas de feature que se integren rápidamente. Usaría `develop` como rama base para features y `main` solo para versiones estables en producción. Las `feature branches` deben ser pequeñas, con cambios bien enfocados, y se integran rápido para evitar desviaciones largas. Las `hotfix branches` se crean directamente desde `main` y se integran tanto a `main` como a `develop` para mantener la sincronización.
    <div align="center">
       <img src="https://i.postimg.cc/ZR4M1bP3/6-35.png" alt="Parte5-1" width="600" />
     </div>

##### **Ejercicio 5: Automatización de reversiones con git en CI/CD**

**Contexto:**  
Durante una integración continua en tu pipeline de CI/CD, se detecta un bug crítico después de haber fusionado varios commits a la rama principal. El equipo necesita revertir los cambios rápidamente para mantener la estabilidad del sistema.

**Pregunta:**  
- ¿Cómo diseñarías un proceso automatizado con Git y CI/CD que permita revertir cambios de manera eficiente y segura? Describe cómo podrías integrar comandos como `git revert` o `git reset` en la pipeline y cuáles serían los pasos para garantizar que los bugs se reviertan sin afectar el desarrollo en curso.
- Ante un bug crítico en la rama principal, usaría `git revert` para deshacer los commits sin reescribir el historial, ya que es más seguro en entornos colaborativos y CI/CD.  Automatizaría esto creando un job en el pipeline que pueda revertir automáticamente los últimos commits marcados como problemáticos.
- Entonces primero se detecta el fallo tras el merge con test automáticos, se lanza el pipeline que ejecute el `git revert`, luego validamos los cambios revertidos con pruebas regresivas y se hace el push, finalmente lo comunicamos al equipo. No usaría  `git reset` ya que estamos en la rama principal y voy afectar su historial perjudicando a mi equipo, a menos, que el bug sea demasiado crítico y se requiera su uso.
--- 

