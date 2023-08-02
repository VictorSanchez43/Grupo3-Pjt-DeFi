# Grupo3-Pjt-DeFi
Este proyecto es de caracter personal tiene todos los derechos reservados.
# De-Fiance Blog

_Este proyecto es un Blog que trata principalmente las Finanzas Descentralizas, temas de Economía y Finanzas en general. 
Se lo contruyó como proyecto final del curso de Desarrollo Web con Python del programa Informatorio de la Provincia del Chaco._

## Comenzando 🚀

_Para obtener una copia del proyecto funcionando en tu PC de manera local para propósitos de desarrollo y pruebas, seguí las instrucciones_


### Pre-requisitos 📋

_Antes de iniciar, es recomendable generar un entorno virtual de trabajo donde instalaremos las dependencias necesarias para que el proyecto funcione. Para ello, abrimos el CMD y nos dirigimos a la carpeta donde queremos guardar el entorno virtual y ejecutamos el siguiente comando:_


```
virtualenv nombre-entorno

```
_Una vez creado es necesario activarlo para ello ejecutamos la siguiente linea (en Windows):_


```
nombre_del_entorno\Scripts\activate.bat

```

_Ya contamos con un entorno virtual activado en el cual podemos instalar todas las dependencias para correr nuestro proyecto._


_Luego, con el entorno activado, no dirigimos a la carpeta donde se encuentra el archivo requirements.txt y ejecuta el siguiente comando en la consola._

```
pip install -r requirements.txt

```
_Este comando instalará en nuestro entorno, todo lo necesario para que el proyecto funcione correctamente._

### SETTINGS 🔧

Luego tenes que crear un archivo de configuraciones en la carpeta Grupo3-Pjt-DeFi\source\proyecto_defi/settings/ y llamala "local.py", donde debes indicar las credenciales de tu base de datos como se muestra a continuacion.

```
from .base import *

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "source", "static"),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'databaseName',
        'USER': 'databaseUser',
        'PASSWORD': 'databasePassword',
        'HOST': 'localhost',
        'PORT': 'portNumber',
    }
}

```


## Construido con 🛠️

_Las herramientas utilizadas para el desarrollo fueron:_

* [Django](https://www.djangoproject.com/) Framework web
* [Python](https://www.python.org/) Del lado del servidor (backend)
* [Bootstrap](https://getbootstrap.com/) Framework web para el desarrollo frontend (HTML, CSS, JavaScript)
* [MySql](https://www.mysql.com/) - Sistema de gestión de bases de datos.


## Autores ✒️

_Proyecto desarrollado por:_ 


✅**Ramón Victor Sánchez**

✅**Ana Laura Ibañez**

✅**Edith Blanco**

✅**Francisco E. Zalazar**


 



También puedes mirar la lista de todos los [contribuyentes](https://github.com/VictorSanchez43/Grupo3-Pjt-DeFi/graphs/contributors) quíenes han participado en este proyecto. 




---
