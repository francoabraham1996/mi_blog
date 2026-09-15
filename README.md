# Mi Blog - Proyecto Final Django

Proyecto final desarrollado con **Python y Django** como parte del curso de Python de Coderhouse.

## Descripción

**Mi Blog** es una aplicación web desarrollada con Django que permite publicar y administrar artículos mediante un sistema de usuarios.

Los visitantes pueden recorrer las publicaciones, utilizar el buscador, consultar la sección "Acerca de mí" y enviar mensajes mediante el formulario de contacto.

Los usuarios registrados pueden iniciar sesión, administrar su perfil y crear sus propios artículos. Cada autor solamente puede editar o eliminar las publicaciones que le pertenecen.

## Funcionalidades

* Registro de usuarios.
* Inicio y cierre de sesión.
* Perfiles de usuario editables.
* Creación de artículos.
* Visualización del detalle de cada artículo.
* Edición de artículos.
* Eliminación de artículos.
* Control de permisos para que cada usuario solamente pueda modificar o eliminar sus propios artículos.
* Buscador de artículos por título.
* Página "Acerca de mí".
* Página de contacto.
* Formulario de contacto con validación.
* Panel de administración de Django.
* Administración de artículos, perfiles y mensajes desde Django Admin.
* Grupo de usuarios "Autores".
* Herencia de templates mediante `base.html`.
* Diseño utilizando Bootstrap y CSS propio.
* Archivos estáticos configurados para deployment.
* Tests básicos automatizados.

## Tecnologías utilizadas

* Python 3.14
* Django 6.0.7
* HTML
* CSS
* Bootstrap
* SQLite
* Git
* GitHub

## Instalación y ejecución local

### 1. Clonar el repositorio

```bash
git clone https://github.com/francoabraham1996/mi_blog.git
```

### 2. Entrar al proyecto

```bash
cd mi_blog
```

### 3. Crear un entorno virtual

```bash
python -m venv .venv
```

### 4. Activar el entorno virtual

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 6. Aplicar las migraciones

```bash
python manage.py migrate
```

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

Una vez iniciado el servidor, la aplicación puede abrirse desde la dirección local indicada por Django en la terminal.

## Tests

El proyecto incluye tests básicos para comprobar el funcionamiento de distintas partes de la aplicación.

Para ejecutarlos:

```bash
python manage.py test
```

Actualmente se comprueban:

* Acceso a la página principal.
* Acceso a la página "Acerca de mí".
* Acceso a la página de contacto.
* Protección de la creación de artículos para usuarios no autenticados.

## Django Admin

El proyecto utiliza el panel de administración de Django para gestionar:

* Artículos.
* Perfiles de usuarios.
* Mensajes recibidos desde el formulario de contacto.

Para utilizar el administrador en una instalación nueva se puede crear un superusuario mediante:

```bash
python manage.py createsuperuser
```

Luego se inicia el servidor y se accede a `/admin/`.

## Estructura principal

```text
mi_blog/
├── blog/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── mi_blog/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Archivos estáticos

El proyecto utiliza archivos estáticos para el diseño del sitio.

La configuración incluye:

```python
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

Para recopilar los archivos estáticos antes de un deployment:

```bash
python manage.py collectstatic --noinput
```

## Deployment

El proyecto se encuentra preparado para realizar un deployment de Django.

Antes de una publicación definitiva se deben configurar los hosts permitidos, las variables de entorno y las opciones de seguridad correspondientes al servicio de hosting utilizado.

**URL pública:** pendiente de configuración.

## Repositorio

Código fuente disponible públicamente en GitHub:

https://github.com/francoabraham1996/mi_blog

## Autor

**Franco Abraham**

Proyecto Final - Python / Django - Coderhouse
