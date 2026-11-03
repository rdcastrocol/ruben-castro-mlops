# Simple ML Training Project

Proyecto para practicar los conocimientos básicos de DevOps.

## Objetivo

El objetivo principal del proyecto no son los códigos, sino los pipelines de CI/CD existentes en la carpeta `.github/workflows/`. Resumidamente, cada uno de ellos hace lo siguiente:

- build.yml: baja un conjunto de datos para entrenar un modelo y lo salva en Azure
- integration.yml: baja el conjunto de datos y el modelo construido por build.yml, para ejecutar un conjunto de pruebas
- deploy.yml: construye una imagen docker de una API simple (presente en la carpeta deployment/app), la sube a un repositorio de DockerHub, se conecta a Azure y carga la imagen desde DockerHub

## Participantes

- Rubén Darío Castro Colmenares
- Eduardo Ernesto Corrales Reyna
- Marc Guillamat
- Federico Zenteno

## Estructura de directorios

```plaintext
ruben-castro-mlops/
├──.github/
|  └──workflows/       # Directorio donde van los pipelines o workflows de GitHub Actions, en formato YAML
├──deployment/         # Directorio para usar con el pipeline deploy.yml
|  ├──app/             # App para hacer deploy
|  └──Dockerfile       # Archivo para construir la imagen Docker
├──scripts/            # Ubicación de scripts auxiliares (en este caso, el script para bajar el modelo de Azure)
├──src/                # Aplicación para entrenar el modelo de ML
├──tests/              # Directorio con los tests para CI
├──.gitignore          # Definición de recursos a ser ignorados por git
├──pytest.ini          # Configuración de los tests
├──README.md           # Documentación del proyecto
└──requirements.txt    # Dependencias del proyecto
```

## Instalación local

1- Clonar el repositorio
2- Entrar en la carpeta del repositorio
3- Crear ambiente virtual de Python: `python -m venv .venv`
4- Activar el ambiente virtual: `source .venv/bin/activate` (en Linux y MacOS, ajustar el comando para Windows)
5- Instalar las dependencias: `python -m pip install -r requirements.txt`

## Ejecución local

Para entrenar el modelo, definir las variables de ambiente en un archivo .env en la raiz y ejecutar `python src/main.py`. Las variables de ambiente necesarias son:

- MLFLOW_URI=...
- EXPERIMENT_NAME=...

Para probar el contenedor con la API, ejecutar los siguientes pasos:

- Entrar en el directorio `deployment`
- Crear las variables de ambiente en un fichero .env
  - MODEL_URI=...
  - MLFLOW_TRACKING_URI=...
- Construir la imagen docker: `docker build -t deploy-app .`
- Inicializar el contenedor: `docker run deploy-app`
- Accesar en `http://localhost:8080`
