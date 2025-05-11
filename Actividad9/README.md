### Actividad: Red-Green-Refactor
**ShoppingCart** debe soportar las siguientes funcionalidades:
- Agregar artículos al carrito
- Eliminar artículos del carrito
- Calcular el total del carrito
- Aplicar descuentos
- Procesar pagos a través de un servicio externo

El desarrollo incremental de `ShoppingCart`esta detallado en `instrucciones.md` por lo cual nos centraremos en ejecutar las pruebas con pytest  para asegurarnos de la correcta implementación de cada funcionalidad.
Obteniendo los siguientes resultados:
 <div align="center">
      <img src="https://i.postimg.cc/XNQSx8VS/8-1.png" alt="Parte1" width="800" />
    </div>


---
### Ejercicio UserManager
El **UserManager** debe:
1. **Agregar usuarios**
2. **Autenticarlos** (usando un servicio de hashing).
3. **Verificar si existen**.
4. **Enviar correos de bienvenida**.
5. **Usar un repositorio de datos (fake)** mediante inyección de dependencias.
6. **Tener pruebas que usen stubs, fakes, mocks y spies**.

Se realizara 6 iteraciones en la metodología TDD **(Red-Green-Refactor)**, cada una introduciendo distintas técnicas.

#### Iteración 1: Agregar usuario
 
#### Red: Escribimos la primera prueba
Creamos una prueba simple que verifica que podemos agregar un usuario con éxito.
**Archivo:** `tests/test_user_manager.py`

```python
import pytest
from user_manager import UserManager, UserAlreadyExistsError

def test_agregar_usuario_exitoso():
    # Arrange
    manager = UserManager()
    username = "kapu"
    password = "securepassword"

    # Act
    manager.add_user(username, password)

    # Assert
    assert manager.user_exists(username), "El usuario debería existir después de ser agregado."
```
Si ejecutamos `pytest`, la prueba fallará porque aún no hemos implementado la clase `UserManager`.

####  Green: 
Implementamos UseManager de forma mínima para que pase la prueba.

**Archivo:** `user_manager.py`

```python
class UserAlreadyExistsError(Exception):
    pass

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UserAlreadyExistsError(f"El usuario '{username}' ya existe.")
        self.users[username] = password

    def user_exists(self, username):
        return username in self.users
```

La prueba pasa exitosamente.

### Refactor: 
Por ahora, el código es claro y cumple su función, por ende no necesitamos refactorizar.

Obtenemos el siguiente resultado:
 <div align="center">
      <img src="https://i.postimg.cc/mgHRQdZb/9-2.png" alt="Parte2" width="800" />
    </div>
    
#### Iteración 2: Autenticación de usuario (Introducción de una dependencia para Hashing)
Ahora para almacenar contraseñas seguras asumiremos que usamos hashes con un servicio de *hashing* mediante inyección de dependencias. 

#### Red: Escribimos la prueba
Crearemos la clase `FakeHashService` que simula un servicio de hashing para poder instanciarla en nuestro`test_autenticar_usuario_exitoso_con_hash()`

**Archivo:** `tests/test_user_manager.py`

```python
class FakeHashService:
    """
    Servicio de hashing 'falso' (Fake) que simplemente simula el hashing
    devolviendo la cadena con un prefijo "fakehash:" para fines de prueba.
    """
    def hash(self, plain_text: str) -> str:
        return f"fakehash:{plain_text}"

    def verify(self, plain_text: str, hashed_text: str) -> bool:
        return hashed_text == f"fakehash:{plain_text}"

def test_autenticar_usuario_exitoso_con_hash():
    # Arrange
    hash_service = FakeHashService()
    manager = UserManager(hash_service=hash_service)

    username = "usuario1"
    password = "mypassword123"
    manager.add_user(username, password)

    # Act
    autenticado = manager.authenticate_user(username, password)

    # Assert
    assert autenticado, "El usuario debería autenticarse correctamente con la contraseña correcta."
```
Al ejecutar el test falla debido a que no hemos implementado ni `authenticate_user` ni la inyección de `hash_service`.
Notar que hemos creado un `FakeHashService` que actúa como un **Fake**: se comporta como un servicio “real”, pero su lógica es simplificada para pruebas (no usa un algoritmo de hashing real).

Si ejecutamos la prueba, fallará porque no hemos implementado ni `authenticate_user` ni la inyección de `hash_service`.

#### Green: Implementamos la funcionalidad y la DI
Para que pase el test pase de forma sencilla inyectaremos el servicio de hashing en UserManager mediante el constructor.
```python
class UserNotFoundError(Exception):
    pass

class UserAlreadyExistsError(Exception):
    pass

class UserManager:
    def __init__(self, hash_service=None):
        """
        Si no se provee un servicio de hashing, se asume un hash trivial por defecto
        (simplemente para no romper el código).
        """
        self.users = {}
        self.hash_service = hash_service
        if not self.hash_service:
            # Si no pasamos un hash_service, usamos uno fake por defecto.
            # En producción, podríamos usar bcrypt o hashlib.
            class DefaultHashService:
                def hash(self, plain_text: str) -> str:
                    return plain_text  # Pésimo, pero sirve de ejemplo.

                def verify(self, plain_text: str, hashed_text: str) -> bool:
                    return plain_text == hashed_text

            self.hash_service = DefaultHashService()

    def add_user(self, username, password):
        if username in self.users:
            raise UserAlreadyExistsError(f"El usuario '{username}' ya existe.")
        hashed_pw = self.hash_service.hash(password)
        self.users[username] = hashed_pw

    def user_exists(self, username):
        return username in self.users

    def authenticate_user(self, username, password):
        if not self.user_exists(username):
            raise UserNotFoundError(f"El usuario '{username}' no existe.")
        stored_hash = self.users[username]
        return self.hash_service.verify(password, stored_hash)
```
Ejecutamos el test y pasa correctamente. 

#### Refactor:
Por ahora la estrucutura cumple el propósito y no es necesario refactorizar.

Obtenemos el siguiente resultado:
 <div align="center">
      <img src="https://i.postimg.cc/TPj6spWF/9-3.png" alt="Parte3" width="800" />
    </div>
    
#### Iteración 3: Uso de un Mock para verificar llamadas (Spy / Mock)
Nuestro objetivo en esta iteración es verificar que `UserManager`  realmente invoque al método `hash`,  cuando agregamos un usuario, para ello usaremos un mock que actuara como “espía”. 

#### Red: Escribimos la prueba de "espionaje"
Usaremos MagicMock que implementa métodos especiales, colecciones, llamadas de comparación, etc.
```python
from unittest.mock import MagicMock

def test_hash_service_es_llamado_al_agregar_usuario():
    # Arrange
    mock_hash_service = MagicMock()
    manager = UserManager(hash_service=mock_hash_service)
    username = "spyUser"
    password = "spyPass"

    # Act
    manager.add_user(username, password)

    # Assert
    mock_hash_service.hash.assert_called_once_with(password)
```
Este test no fallara debido a que nuestro código ya llama a `hash_service.hash`.

#### Green:
Por lo mencionado anteriormente, el test pasa exitosamente.

#### Refactor:
Solo corroboramos el comportamiento interno por lo cual no es necesario refactorizar.

Obtenemos el siguiente resultado:
 <div align="center">
      <img src="https://i.postimg.cc/Gttn9KSn/9-4.png" alt="Parte4" width="800" />
    </div>
    
#### Iteración 4: Excepción al agregar usuario existente (Stubs/más pruebas negativas)
Forzaremos que `user_exists` devuelva `True` mediante un stub sin necesidad de preparar el estado interno del diccionario `users` para asi poder probar de forma rápida y sencilla el caso en que no se debe poder agregar un usuario ya existente.
#### Red: Escribimos las prueba

```python
def test_no_se_puede_agregar_usuario_existente_stub():
    # Este stub forzará que user_exists devuelva True
    class StubUserManager(UserManager):
        def user_exists(self, username):
            return True

    stub_manager = StubUserManager()
    with pytest.raises(UserAlreadyExistsError) as exc:
        stub_manager.add_user("cualquier", "1234")

    assert "ya existe" in str(exc.value)
```
El test fallará debido a que se fuerza a que `user_exists` devuelva `True`; sin embargo, en nuestro método `add_user` no usamos `user_exists`.
#### Green:  
Modificaremos `add_user` para que use `user_exists`.
```py
    def add_user(self, username, password):
        # verificamos mediante user_exists
        if self.user_exists(username): 
            raise UserAlreadyExistsError(f"El usuario '{username}' ya existe.")
        hashed_pw = self.hash_service.hash(password)
        self.users[username] = hashed_pw
```


#### Refactor:
No es necesario refactorizar.
Obtenemos el siguiente resultado:
 <div align="center">
      <img src="https://i.postimg.cc/nrWbmm6j/9-5.png" width="800" />
    </div>


#### Iteración 5: Agregar un "Fake" repositorio de datos (Inyección de Dependencias)
Hasta ahora guardamos usuarios en un diccionario, en el caso que queramos usar una base de datos pero para las pruebas un repositorio en memoria, debemos usar **Fake** o **InMemory**.
#### Red: 
Creamos una prueba que verifique que podemos inyectar un repositorio y que `UserManager` lo use.

```python
class InMemoryUserRepository:
    """Fake de un repositorio de usuarios en memoria."""
    def __init__(self):
        self.data = {}

    def save_user(self, username, hashed_password):
        if username in self.data:
            raise UserAlreadyExistsError(f"'{username}' ya existe.")
        self.data[username] = hashed_password

    def get_user(self, username):
        return self.data.get(username)

    def exists(self, username):
        return username in self.data

def test_inyectar_repositorio_inmemory():
    repo = InMemoryUserRepository()
    manager = UserManager(repo=repo)  # inyectamos repo
    username = "fakeUser"
    password = "fakePass"

    manager.add_user(username, password)
    assert manager.user_exists(username)
```
Este test falla porque aún no modificamos `UserManager` para que reciba un `repo`.

#### Green: Implementación
Modificamos `UserManager` para que reciba un `repo`, y por defecto simularemos una base de datos en memoria que nos permitirá correr los tests rápido.

```python
class UserManager:
    def __init__(self, hash_service=None, repo=None):
        self.hash_service = hash_service or self._default_hash_service()
        self.repo = repo or self._default_repo()
    
    def _default_hash_service(self):
        class DefaultHashService:
            def hash(self, plain_text: str) -> str:
                return plain_text
            def verify(self, plain_text: str, hashed_text: str) -> bool:
                return plain_text == hashed_text
        return DefaultHashService()

    def _default_repo(self):
        # Un repositorio en memoria muy básico
        class InternalRepo:
            def __init__(self):
                self.data = {}
            def save_user(self, username, hashed_password):
                if username in self.data:
                    raise UserAlreadyExistsError(f"'{username}' ya existe.")
                self.data[username] = hashed_password
            def get_user(self, username):
                return self.data.get(username)
            def exists(self, username):
                return username in self.data
        return InternalRepo()

    def add_user(self, username, password):
        if self.user_exists(username):
            raise UserAlreadyExistsError(f"El usuario '{username}' ya existe.")
        hashed = self.hash_service.hash(password)
        self.repo.save_user(username, hashed)

    def user_exists(self, username):
        return self.repo.exists(username)

    def authenticate_user(self, username, password):
        stored_hash = self.repo.get_user(username)
        if stored_hash is None:
            raise UserNotFoundError(f"El usuario '{username}' no existe.")
        return self.hash_service.verify(password, stored_hash)
```
Al ejecutar el test pasa exitosamente.

#### Refactor:
Hasta el momento no es necesario refactorizar.

Obteniendo el siguiente resultado:
 <div align="center">
      <img src="https://i.postimg.cc/h4ZqNFfD/9-6.png" alt="Parte6" width="800" />
    </div>

#### Iteración 6: Introducir un “Spy o Mock” de notificaciones (Envío de correo)
Adicionaremos una nueva funcionalidad para enviar un correo de bienvenida a los nuevos usuarios agregados.
Finalmente, agregaremos una funcionalidad que, cada vez que se agrega un usuario, se envíe un correo de bienvenida. Para probar este envío de correo sin mandar correos reales, usaremos un **Spy** o **Mock** que verifique que se llamó al método `send_welcome_email` con los parámetros correctos.

#### Red: Prueba
Para realizar la prueba usaremos un **Mock** que verifique que se llamó al método `send_welcome_email` con los parámetros correctos, que a diferencia de un **Spy** que es un mock que además envuelve (wraps) a un objeto real, de modo que ejecuta su lógica interna y al mismo tiempo registra la llamada.
```python
def test_envio_correo_bienvenida_al_agregar_usuario():
    # Arrange
    mock_email_service = MagicMock()
    manager = UserManager(email_service=mock_email_service)
    username = "nuevoUsuario"
    password = "NuevaPass123!"

    # Act
    manager.add_user(username, password)

    # Assert
    mock_email_service.send_welcome_email.assert_called_once_with(username)
```
El test fallará porque `UserManager` aún no recibe ningun correo.

#### Green: Implementamos la llamada al servicio de correo

Modificamos `UserManager` para que reciba un correo y se llame al método `send_welcome_email` cada vez que se realiza `add_user`.
```python
class UserManager:
    def __init__(self, hash_service=None, repo=None, email_service=None):
        self.hash_service = hash_service or self._default_hash_service()
        self.repo = repo or self._default_repo()
        self.email_service = email_service

    def add_user(self, username, password):
        hashed = self.hash_service.hash(password)
        self.repo.save_user(username, hashed)
        if self.email_service:
            self.email_service.send_welcome_email(username)
```
El test pasa exitosamente.
#### Refactor
Dado que simplemente inyectamos `email_service` y agregamos la llamada al método en `add_user`, no es necesario refactorizar.

Obteniendo los siguientes resultados finales:
 <div align="center">
      <img src="https://i.postimg.cc/L6rF6ztG/9-7.png" alt="Parte7" width="800" />
    </div>

