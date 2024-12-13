# App bajío

<p align="center">
  <img src="https://i.ibb.co/64rmBtF/rgv.png" alt="RGV logo" title="RGV logo" />
</p>

## Estructura del proyecto

```
.
├── .github
│   └── workflows
├── python
│   ├── forms
│   ├── models
│   ├── routes
│   └── services
├── static
│   ├── css
│   ├── images
│   ├── js
│   └── queries
├── templates
│   ├── authentication
│   ├── forms
│   ├── functionalities
│   ├── main
│   ├── pages
│   └── partials
├── .env
├── .gitignore
├── app.py
├── Procfile
├── README.md
└── requirements.txt
```

## Descripción de los archivos y carpetas

- `app`: Carpeta que contiene el código de la aplicación.
  - `__init__.py`: Archivo que inicializa la aplicación.
  - `models.py`: Archivo que contiene las definiciones de las tablas de la base de datos.
  - `routes.py`: Archivo que contiene las rutas de la aplicación.
  - `templates`: Carpeta que contiene las plantillas HTML de la aplicación.
- `config.py`: Archivo que contiene la configuración de la aplicación.
- `instance`: Carpeta que contiene la configuración de la instancia de la aplicación.
- `migrations`: Carpeta que contiene las migraciones de la base de datos.
- `README.md`: Archivo que contiene la descripción de la estructura de carpetas.
- `requirements.txt`: Archivo que contiene las dependencias de la aplicación.
- `run.py`: Archivo que inicializa la aplicación.

## Ejecución de la aplicación

Para ejecutar la aplicación, se deben seguir los siguientes pasos:

1. Crear un entorno virtual:

Windows:

```bash
python3 -m venv venv
```

Linux y macOS:

```bash
python -m venv venv
```

2. Activar el entorno virtual:

Windows:

```bash
venv\Scripts\activate
```

Linux y macOS:

```bash
source venv/bin/activate
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

4. Variables de entorno:

Crear un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:

```bash
# database configuration
DB_USER=postgres
DB_PASSWORD=password # cambiar por la contraseña de la base de datos
DB_HOST=localhost # cambiar por la dirección de la base de datos
DB_NAME=db_name # cambiar por el nombre de la base de datos 
DB_PORT=5432
# email configuration
EMAIL_USER=email # cambiar por el correo electrónico
EMAIL_PASSWORD=password # cambiar por la contraseña del correo electrónico (app password)
```

5. Inicializar la base de datos (si es necesario):

```bash
flask db init
flask db migrate
flask db upgrade
```

¿Cuándo inicializar la base de datos?

- Si se creará una nueva base de datos en AWS RDS.
- Si se desea crear una base de datos local.

6. Ejecutar la aplicación:

```bash
flask run
```

## Despliegue a AWS usando GitHub Actions

Para desplegar la aplicación a AWS usando GitHub Actions, se deben seguir los siguientes pasos:

1. El proyecto ya contiene un archivo de configuración de GitHub Actions llamado `deploy.yml` que se encarga de desplegar la aplicación a AWS.

2. Crear una aplicación en AWS Elastic Beanstalk.

3. Configurar las variables de entorno en GitHub con las credenciales de AWS.

4. Hacer un push a la rama `main` del repositorio.

5. GitHub Actions se encargará de desplegar la aplicación en AWS Elastic Beanstalk.

### Variables de entorno de GitHub

#### Secrets

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

#### Variables

- `APPLICATION_NAME`
- `AWS_REGION`
- `ENVIRONMENT_NAME`
- `S3_BUCKET`

### Variables de entorno de AWS Elastic Beanstalk

- `FLASK_ENV`: `production`
- `FLASK_APP
- `SECRET_KEY
- `DATABASE_URL`

## Información adicional

### Plantilla frontend

La plantilla frontend de la aplicación usa Alpine.js y Tailwind CSS. Se encuentra en el siguiente [enlace (drive)](https://drive.google.com)

### Actualizar dependencias

Actualizar dependencias

```bash
pip freeze > requirements.txt
```

### Tipos de alertas flash

Estas son las clases de alertas flash que se pueden utilizar compatibles con la plantilla frontend:

- `primary`
- `purple`
- `success`
- `warning`
- `danger`
- `gray`

### Contraseña de aplicación de Google (app password)

La contraseña de aplicación de Google se puede generar en el siguiente [enlace](https://myaccount.google.com/apppasswords)
