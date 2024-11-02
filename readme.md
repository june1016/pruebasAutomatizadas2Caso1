````markdown
# Gestión de Tareas - Aplicación y Pruebas Automatizadas

Este proyecto es una aplicación web sencilla para gestionar tareas personales, que permite agregar, editar, marcar como completadas y eliminar tareas. La aplicación está desarrollada con HTML, CSS y JavaScript, y cuenta con pruebas automatizadas creadas en Python con Selenium.

## Requisitos Previos

1. **Python 3.x** instalado en el sistema.
2. **Google Chrome** instalado (o el navegador que prefieras usar con Selenium).
3. **ChromeDriver** para Chrome (o el WebDriver correspondiente a tu navegador).
4. **Entorno Virtual** para manejar las dependencias (opcional, pero recomendado).

## Configuración Inicial

### 1. Clonar el Repositorio

Clona este repositorio en tu máquina local:

```bash
git https://github.com/june1016/pruebasAutomatizadas2Caso1.git
cd https://github.com/june1016/pruebasAutomatizadas2Caso1.git
```
````

### 2. Crear un Entorno Virtual

Crea y activa un entorno virtual para aislar las dependencias del proyecto:

```bash
python -m venv venv
```

En Windows:

```bash
venv\Scripts\activate
```

En macOS y Linux:

```bash
source venv/bin/activate
```

### 3. Instalar Dependencias

Instala las dependencias necesarias usando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` debe incluir las siguientes dependencias:

```
selenium
webdriver-manager
```

### 4. Descargar y Configurar el WebDriver

Este proyecto utiliza **webdriver-manager** para manejar automáticamente la descarga del ChromeDriver, que Selenium necesita para interactuar con el navegador. No es necesario configurar manualmente el WebDriver, ya que se administrará automáticamente al ejecutar las pruebas.

## Ejecución de la Aplicación

### 1. Iniciar el Servidor Local

Para ejecutar la aplicación, inicia un servidor local. Navega a la carpeta raíz del proyecto (donde se encuentra `index.html`) y ejecuta:

```bash
python -m http.server 8000
```

Esto iniciará el servidor en `http://localhost:8000`.

### 2. Verificar la Aplicación

Abre tu navegador y navega a `http://localhost:8000` para verificar que la aplicación esté funcionando correctamente. Deberías ver una interfaz para agregar, editar, marcar como completadas y eliminar tareas.

## Ejecución de Pruebas Automatizadas

Este proyecto incluye pruebas automatizadas en Python utilizando Selenium para verificar el funcionamiento de la aplicación.

### 1. Configurar el Servidor

Asegúrate de que el servidor local esté corriendo en `http://localhost:8000` antes de ejecutar las pruebas. Las pruebas dependen de que la aplicación esté accesible en esta dirección.

### 2. Ejecutar las Pruebas

Para ejecutar las pruebas, asegúrate de que el entorno virtual esté activado y que el servidor esté en funcionamiento. Navega a la carpeta `tests` y ejecuta los scripts de prueba:

```bash
python tests\CasoPrueba1.1.py
python tests\CasoPrueba1.2.py
python tests\CasoPrueba2.1.py
python tests\CasoPrueba2.2.py
python tests\CasoPrueba3.1.py
python tests\CasoPrueba3.2.py
python tests\CasoPrueba4.1.py
python tests\CasoPrueba5.1.py
python tests\CasoPrueba5.2.py
```

Cada script de prueba generará una salida en la consola que indica si el caso de prueba pasó o falló.
