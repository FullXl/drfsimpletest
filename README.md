Este proyecto es una API simple desarrollada con Django REST Framework (DRF). Implementa un sistema CRUD para gestionar proyectos y está protegida con autenticación basada en tokens JWT (JSON Web Tokens) utilizando SimpleJWT.

Requisitos Previos
Antes de comenzar, asegúrate de tener instalado lo siguiente:

Python 3.8 o superior
pip (el gestor de paquetes de Python)
Virtualenv (opcional, pero recomendado)
Instalación
Sigue estos pasos para configurar el proyecto en tu entorno local:

Clona el Repositorio

bash
Copiar código
git clone <URL-del-repositorio>
cd drfsimplecrud
Crea un Entorno Virtual

bash
Copiar código
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
Instala las Dependencias

bash
Copiar código
pip install -r requirements.txt
Aplica las Migraciones

bash
Copiar código
python manage.py migrate
Crea un Superusuario

bash
Copiar código
python manage.py createsuperuser
Inicia el Servidor de Desarrollo

bash
Copiar código
python manage.py runserver
La API estará disponible en http://127.0.0.1:8000/.

Endpoints
Autenticación
Obtener Token de Acceso y Refresco

css
Copiar código
POST /api/token/
Body:
{
    "username": "<usuario>",
    "password": "<contraseña>"
}
Refrescar Token

css
Copiar código
POST /api/token/refresh/
Body:
{
    "refresh": "<token_de_refresco>"
}
Verificar Token

css
Copiar código
POST /api/token/verify/
Body:
{
    "token": "<token_de_acceso>"
}
CRUD de Proyectos
Listar Proyectos (Requiere autenticación JWT)

bash
Copiar código
GET /api/projects/
Crear un Proyecto (Requiere autenticación JWT)

css
Copiar código
POST /api/projects/
Body:
{
    "name": "Nuevo Proyecto",
    "description": "Descripción del proyecto"
}
Actualizar un Proyecto (Requiere autenticación JWT)

bash
Copiar código
PUT /api/projects/<id>/
Body:
{
    "name": "Proyecto Actualizado",
    "description": "Nueva descripción"
}
Eliminar un Proyecto (Requiere autenticación JWT)

bash
Copiar código
DELETE /api/projects/<id>/
Estructura del Proyecto
bash
Copiar código
drfsimplecrud/
│
├── drfsimplecrud/
│   ├── settings.py         # Configuración principal del proyecto
│   ├── urls.py             # Rutas principales
│   ├── wsgi.py             # Servidor WSGI
│   └── asgi.py             # Servidor ASGI
│
├── proyects/
│   ├── migrations/         # Migraciones de base de datos
│   ├── api.py              # Vistas del CRUD
│   ├── models.py           # Modelos de la base de datos
│   ├── serializers.py      # Serializadores de DRF
│   ├── urls.py             # Rutas de la app
│   └── views.py            # Vistas adicionales
│
├── db.sqlite3              # Base de datos SQLite (no usar en producción)
├── requirements.txt        # Dependencias del proyecto
├── manage.py               # Comando para manejar el proyecto
└── README.md               # Documentación del proyecto
Dependencias
El archivo requirements.txt incluye:

Django
Django REST Framework
Django REST Framework SimpleJWT
dj-database-url
Whitenoise (para manejar archivos estáticos en producción)
Autenticación JWT
Este proyecto utiliza JWT (JSON Web Tokens) para proteger los endpoints. Para acceder a los endpoints protegidos, sigue estos pasos:

Obtén un token de acceso enviando las credenciales al endpoint /api/token/.
Usa el token de acceso en el encabezado Authorization de tus solicitudes:
makefile
Copiar código
Authorization: Bearer <token_de_acceso>
Renueva el token de acceso cuando expire usando el endpoint /api/token/refresh/.
Notas para Producción
Configura una base de datos adecuada, como PostgreSQL.
Establece una clave secreta segura (SECRET_KEY) en variables de entorno.
Configura DEBUG = False en producción.
Usa un servidor WSGI como Gunicorn y un servidor proxy como Nginx.
Contribuciones
Si deseas contribuir a este proyecto, por favor:

Crea un fork del repositorio.
Realiza tus cambios en una rama separada.
Envía un pull request con una descripción detallada de tus cambios.
Licencia
Este proyecto está bajo la Licencia MIT. Puedes usarlo libremente para propósitos personales o comerciales.
