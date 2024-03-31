# Información sobre la API
Esta API **solo usa** el metodo HTTP POST.

## API Endpoint
Django correra por defecto el servidor en localhost con puerto 8000 (127.0.0.1:8000).

http://127.0.0.1:8000/**endpoint**

**signup**
**login**

### Signup / Registro de usuario 
Para crear una cuenta en el servidor
el cliente debe proporcionar la siguiente informacion:
+ username (nombre de usuario)
+ password (contraseña)
+ email (correo electrónico)


### login / Autenticación basica
Para iniciar sesión el cliente de la API debe proporcionar la siguiente información:
+ username (nombre de usuario)
+ password (contraseña)  


### Envio de datos
En el body de la petición enviamos la información de registro, o de inicio de sesión.
Los datos se envian en formato **JSON**.

**Ejemplo de Signup / Registro de usuario**
"username": "Lilit01",
"password": "P12345P",
"email": "lilit_apple@gmail.com"

### CÓDIGO DE ESTADO HTTP
**200** _OK_ La solicitud ha tenido éxito.

**201** _OK_ Indica que la solicitud ha tenido éxito y ha llevado a la creación de un recurso.

**400** _Bad Request_ La solicitud era inaceptable, a menudo porque faltaba un parámetro obligatorio.

**404** _Not Found_ El recurso solicitado no existe.

