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
- Esto es útil para la revisión del sprint, ya que el equipo puede mostrar avances reales sin comprometer estabilidad ni fusionar código incompleto. También facilita que el equipo de QA o los stakeholders prueben algo funcional, mientras el resto del trabajo sigue aún en progreso.

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
 
**Desventajas:**
- Conflictos para los colaboradores sino están familiarizados.
- Fusiones complejas en caso una rama pública ha sido rebased y se ha alterado el historial.
- Pérdida de contexto al aplatas commits.
---

### **Navegando conflictos y versionado en un entorno devOps**
