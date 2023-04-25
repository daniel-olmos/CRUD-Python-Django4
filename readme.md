# CRUD Python-Django4

En todo proyecto es importante primero crear un entorno virtual para que tanto la versión de Python, Django y demás librerías se queden aisladas, ya que por ejempo, si instalas una nueva versión de Python o Django e intentas correr este proyecto que vamos a crear, pues no va funcionar por la imcompatibilidad de versiones. Y si tenemos nuestro proyecto, siempre en un entorno virtual, pues lograremos que funcione con la misma versión de Python, Django y demás librerías con que fue creado el proyecto.

Creo un directorio con el nombre cruddjango4, en donde colocaré todos los archivos de mi proyecto.



```
// Directorio con el nombre "cruddjango4" 
 
/cruddjango4
  ... Acá irán todos los archivos del proyecto
  ...
  ...
```

Usaré el paquete virtualenv para crear mi entorno virtual. Para instalarlo voy a mi consola de comandos y ejecuto el siguiente comando:

```
# Comando para crear un entorno virtual con el paquete 'virtualenv' 
python -m venv miev  
```

Luego de ejecutar el comando anterior, se me ha creado un directorio llamado miev.

```
/cruddjango4 
  ├── /miev // Se creó este directorio
```
Ahora debemos activar nuestro entorno virtual ejecutando el siguiente comando:
```
# Comando para activar el entorno virtual 
source miev/Scripts/activate
```
Luego que el entorno virtual se activa, aparece en la consola o terminal, entre parentesis el nombre del entorno virtual, es decir: (miev).

NOTA: Recuerda que siempre debes activar tu entorno virtual, antes de continuar trabajando en un proyecto con Django.

## Creación de Nuevo Proyecto

Primero debemos instalar Django, ejecutamos el siguiente comando para instalarlo:
```
pip install django
```
Paso seguido, creo un nuevo proyecto para el sistema CRUD, le pondré de nombre cruddjango4, ejecuto el siguiente comando en mi consola de comandos.

```
django-admin startproject cruddjango4
```
Tras ejecutar el comando anterior, no pasa nada en la consola o terminal, pero Django nos ha creado un directorio con el nombre del proyecto y en el contiene directorios y archivos necesarios para que nuestro proyecto funcione sin problemas.

```
/cruddjango4 
    ├── /cruddjango31 // Django nos creo este directorio con ciertos archivos en su interior 
        ├── __init__.py 
        ├── asgi.py 
        ├── settings.py 
        ├── urls.py 
        ├── wsgi.py        
    ├── manage.py
├── /miev
```
Para verificar que el proyecto se ha creado correctamente, ingresamos al directorio del proyecto y allí arrancaremos el servidor local de Django Framework ejecutando el siguiente comando.
```
# Ingresamos al directorio del proyecto 
cd cruddjango4  
 
# Ejecutamos el servidor local de Django 
python manage.py runserver 
```

Si vamos al navegador y abrimos la ruta local http://localhost:8000/ puedo ver el proyecto por defecto que Django nos ha creado.

El proyecto se ha creado correctamente. Ahora en Django necesitamos crear un nuevo modulo o aplicación para nuestro sistema CRUD, yo trabajaré con datos de jugos entonces a mi aplicación le pondré de nombre jugos y lo crearé ejecutando el siguiente comando:
```
# Comando para crear la aplicación 'jugos' 
python manage.py startapp jugos
```

Al ejecutar el comando anterior, no ha pasado nada en la consola o terminal, pero si vamos al directorio del proyecto podemos ver que se nos ha creado un directorio llamado jugos y en el podemos encontrar un directorio llamado migrations con varios archivos necesarios para que la aplicación funcione correctamente.

 ```
/cruddjango4 
    ├── /cruddjango4
    ├── /jugos // Se ha creado este directorio 'jugos' 
        ├── /migrations 
        ├── __init__.py 
        ├── admin.py 
        ├── apps.py 
        ├── models.py 
        ├── tests.py 
        ├── views.py 
    ├── db.sqlite3
    ├── manage.py 
├── /miev
```

Para que la aplicación jugos, funcione en Django debemos de registrarla en el archivo llamado settings.py, este archivo se encuentra en cruddjango4 > cruddjango4 > cruddjango4 > settings.py 

 ```
/cruddjango4 
    ├── /cruddjango4        
        ├── __init__.py
        ├── asgy.py
        ├── settings.py // Abro este Archivo 
        ├── urls.py
        ├── wsgi.py
    ├── /jugos
    ├── db.sqlite3
    ├── manage.py 
├── /miev
```

Abro el archivo settings.py y voy a la sección que dice INSTALLED_APPS y registro la app jugos. 
```
# Registro la app 'postres' en el archivo  settings.py 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jugos', # Registramos la app 'jugos' 
]
```
## Base de Datos

Voy a usar MySQL como base de datos. Instalo el paquete mysqlclient que da soporte a Django Framework para usar MySQL. Ejecuto el siguiente comando: 


```
pip install mysqlclient 
```

Estoy usando Laragon como servidor local, esta herramienta viene con MySQL. Voy a crear la base de datos, la llamaré cruddjango y dentro de ella creare la tabla llamada jugos, esta tabla va tener los campos id, nombre, precio, stock, img, created_at y updated_at. Como sabemos el campo id debe ser Autoincrementable, este se genera automáticamente cuando haga la migración en Django para la tabla jugos.

Defino los campos que va tener la tabla jugos, abro el archivo llamado models.py que se encuentra en el directorio llamado también jugos:

```
/cruddjango4 
    ├── /cruddjango4 
    ├── /jugos 
        ├── __pycache__
        ├── __init__.py
        ├── admin.py
        ├── apps.py 
        ├── models.py // Abro este Archivo 
        ├── tests.py 
        ├── views.py
    ├── db.sqlite3
    ├── manage.py 
├── /miev
```

Tras abrir el archivo models.py le agrego los siguientes campos para la tabla jugos:

```
from django.db import models
from django.utils import timezone
 
# Creación de campos de la tabla 'jugos' 
class Jugos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=20)
    stock = models.CharField(max_length=100)
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
         db_table = 'jugos' # Le doy de nombre 'jugos' a nuestra tabla en la Base de Datos 
```
En el código anterior, he definido los campos id, nombre, precio, stock, img, created_at y updated_at para la tabla jugos.

Antes de ejecutar las migraciones, debemos configurar la base de datos en el archivo de configuración de Django llamado settings.py, este archivo se encuentra en la carpeta cruddjango4 >cruddjango4 >cruddjango4 

```
/cruddjango4 
    ├── /cruddjango4  
        ├── __pycache__
        ├── __init__.py
        ├── asgi.py
        ├── settings.py // Abro este Archivo 
        ├── urls.py 
        ├── wsgi.py
    ├── /jugos  
    ├── db.sqlite3
    ├── manage.py 
├── /miev
```
Dentro del archivo settings.py agrego soporte y conexión a la base de datos MySQL, ya que usaré la base de datos MySQL, le colocaré el termino ‘default’ para indicarle a Django que MySQL será el motor que usaré como base de datos y debajo coloco el nombre de mi base de datos, usuario, password  y como opción le digo a Django que usaré el modo SQL tradicional. 

```
DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'default': { # le coloco default para poder usar MySQL 
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cruddjango',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}
```
Ahora voy a crear la migración de la tabla jugos, en mi consola de comandos y ejecuto el siguiente comando: 
```
python manage.py makemigrations jugos 
```
Bien ahora procederé a crear la tabla jugos en la base de datos, ejecuto el siguiente comando en mi consola de comandos.
```
python manage.py migrate jugos 
```
Si me dirijo a la base de datos puedo ver que se me ha creado la tabla jugos con los campos que le especifique.

## Vistas Genéricas

Django Framework trabaja sobre la arquitectura MTV (Model Template View) que traducido al español significa Modelo Plantilla Vista. Cuando creamos este proyecto, Django nos generó un archivo llamado views.py en donde podemos definir las vistas y otras tares para nuestro proyecto. Django nos permite trabajar con vistas genéricas de su propio core, estas vistas genéricas nos permiten realizar de manera ágil ciertas tareas en nuestro proyecto sin escribir mucho código.

El termino CRUD significa Create, Read, Update y Delete, por ende usaré las siguientes vistas genéricas:

- ListView (Para listar en la vista principal, todos los registros de la tabla jugos)
- DetailView (Leer)
- CreateView (Crear)
- UpdateView (Actualizar)
- DeleteView (Eliminar)

Abro el archivo llamado views.py que se encuentra en cruddjango4 > jugos > views.py 

```
/cruddjango4 
    ├── /cruddjango4  
    ├── /jugos 
        ├── /__pycache__
        ├── /migrations
        ├── /static
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        ├── views.py // Abro este archivo 
    ├── db.sqlite3
    ├── manage.py 
├── /miev
```
En el archivo views.py instancio las vistas genéricas de Django y mi modelo Jugos el cual configuramos dentro del archivo models.py

```
from django.shortcuts import render
 
# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
# Instanciamos el modelo 'Jugos' para poder usarlo en nuestras Vistas CRUD
from .models import Jugos
```
Ahora voy a instanciar 3 utilidades necesarias para este proyecto, estas son reverse, messages y forms. He colocado comentarios para explicar que hace cada una de ellas: 

```
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms
```
Paso seguido, crearé unas clases para poder usar las vistas genéricas de Django: ListView, DetailView, CreateView, UpdateView y DeleteView.

## Listado de Registros o Jugos
En esta vista vamos a mostrar en una tabla de la vista principal, todos los registros almacenados en la base de datos del sistema CRUD. Creo una clase con el nombre JugosListado la cual usará la vista genérica ListView: 

```
class JugosListado(ListView): 
    model = Jugos # Llamamos a la clase 'Jugos' que se encuentra en nuestro archivo 'models.py'
```
Ahora crearé las vistas para las tareas CRUD (CRUD son Create, Read, Update y Delete). 

## Crear (Create)

Creo una clase con el nombre JugoCrear que usará la vista genérica CreateView en donde mostraremos un formulario para crear un nuevo registro o jugo, en el código colocare unos comentarios que explican para que sirve cada línea del código:

```python
class JugoCrear(SuccessMessageMixin, CreateView): 
    model = Jugos # Llamamos a la clase 'Jugos' que se encuentra en nuestro archivo 'models.py'
    form = Jugos # Definimos nuestro formulario con el nombre de la clase o modelo 'Jugos'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'jugos' de nuestra Base de Datos 
    success_message = 'Jugo Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Jugo
 
    # Redireccionamos a la página principal luego de crear un registro o jugo
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
```

## Leer (Read)
Para esta tarea creo una clase con el nombre JugoDetalle que usará la vista genérica DetailView la cual se encargará de mostrar los detalles de un jugo o registro: 
```
class JugoDetalle(DetailView): 
    model = Jugos # Llamamos a la clase 'Jugos' que se encuentra en nuestro archivo 'models.py'
```
## Actualizar (Update)

Creo una clase con el nombre JugoActualizar que usará la vista genérica UpdateView, en esta vista mostraremos un formulario para actualizar un jugo o registro, obviamente de la Base de Datos. Asimismo en el código colocare unos comentarios que explican para que sirve cada línea del código:
```
 
class JugoActualizar(SuccessMessageMixin, UpdateView): 
    model = Jugos # Llamamos a la clase 'Jugos' que se encuentra en nuestro archivo 'models.py' 
    form = Jugos # Definimos nuestro formulario con el nombre de la clase o modelo 'Jugos' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'jugos' de nuestra Base de Datos 
    success_message = 'Jugo Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Jugo 
 
    # Redireccionamos a la página principal luego de actualizar un registro o jugo 
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
```

## Eliminar (Delete)
Por último creo una clase con el nombre JugoEliminar que hara uso de la vista genérica DeleteView, esta vista la usaremos para eliminar un registro o jugo de nuestra base de datos, especificamente de la tabla jugos:

```
 
class JugoEliminar(SuccessMessageMixin, DeleteView): 
    model = Jugos 
    form = Jugos
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o jugo
    def get_success_url(self): 
        success_message = 'Jugo Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Jugo
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
```
A continuación el código completo del archivo views.py: 
```

from django.shortcuts import render

# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
# Instanciamos el modelo 'Jugos' para poder usarlo en nuestras Vistas CRUD
from .models import Jugos 

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms


class JugosListado(ListView): 
    model = Jugos # Llamamos a la clase 'Jugos' que se encuentra en nuestro archivo 'models.py' 

class JugoCrear(SuccessMessageMixin, CreateView): 
    model = Jugos # Llamamos a la clase 'Jugos' que se encuentra en nuestro archivo 'models.py'
    form = Jugos # Definimos nuestro formulario con el nombre de la clase o modelo 'Jugos'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'jugos' de nuestra Base de Datos 
    success_message = 'Jugo Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Jugo
 
    # Redireccionamos a la página principal luego de crear un registro o jugo
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class JugoDetalle(DetailView): 
    model = Jugos # Llamamos a la clase 'Jugos' que se encuentra en nuestro archivo 'models.py' 


class JugoActualizar(SuccessMessageMixin, UpdateView): 
    model = Jugos # Llamamos a la clase 'Jugos' que se encuentra en nuestro archivo 'models.py' 
    form = Jugos # Definimos nuestro formulario con el nombre de la clase o modelo 'Jugos' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'jugos' de nuestra Base de Datos 
    success_message = 'Jugo Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Jugo 
 
    # Redireccionamos a la página principal luego de actualizar un registro o jugo 
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'


class JugoEliminar(SuccessMessageMixin, DeleteView): 
    model = Jugos 
    form = Jugos
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o jugo
    def get_success_url(self): 
        success_message = 'Jugo Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Jugo
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

```
## Rutas
Para el sistema CRUD voy a crear 5 rutas indispesables para que funcione sin problemas. Abro el archivo urls.py que se encuentra en cruddjango4 > cruddjango4 > urls.py 

```
/cruddjango4  
    ├── /cruddjango4  
        ├── __init__.py 
        ├── asgi.py 
        ├── settings.py 
        ├── urls.py // Abro este archivo 
        ├── wsgi.py 
    ├── /jugos
    ├── db.sqlite3
    ├── manage.py 
├── /miev
```
En el archivo urls.py agrego las siguientes rutas dentro de urlpatterns = [], mediante estas rutas llamamos a una determinada vista HTML, estas vistas HTML las crearé más adelante.

La ruta admin/ la creo el Framework Django automáticamente cuando se creo el proyecto, asi que no hay que tocarla.

```

urlpatterns = [ 
    
    path('admin/', admin.site.urls), 

    # La ruta 'leer' en donde listamos todos los registros o jugos de la Base de Datos
    path('jugos/', JugosListado.as_view(template_name = "jugos/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un jugo o registro 
    path('jugos/detalle/<int:pk>', JugoDetalle.as_view(template_name = "jugos/detalles.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo jugo o registro  
    path('jugos/crear', JugoCrear.as_view(template_name = "jugos/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un jugo o registro de la Base de Datos 
    path('jugos/editar/<int:pk>', JugoActualizar.as_view(template_name = "jugos/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un jugo o registro de la Base de Datos 
    path('jugos/eliminar/<int:pk>', JugoEliminar.as_view(), name='eliminar'), 

]

```

Con las rutas que definí en el código anterior, estoy llamando a las vistas genéricas (clases) que definimos en la Parte 3 de este tutorial, por ejemplo en la ruta jugos/crear llamamos a la clase JugoCrear la cual debe llamar al template o vista crear.html que se encuentra dentro de la carpeta jugos y al final le asignamos un nombre a esta ruta, el nombre que le asignamos es crear.

Se puede apreciar que las rutas detalle, actualizar y eliminar usan el id del jugo o registro que es un dato de tipo int

```

# La ruta 'detalles' en donde mostraremos una página con los detalles de un jugo o registro 
path('jugos/detalle/<int:pk>', JugosDetalle.as_view(template_name = "jugos/detalles.html"), name='detalles'),
 
# La ruta 'crear' en donde mostraremos un formulario para crear un nuevo jugo o registro  
path('jugos/crear', JugoCrear.as_view(template_name = "jugos/crear.html"), name='crear'),
 
# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un jugo o registro de la Base de Datos 
path('jugos/editar/<int:pk>', JugoActualizar.as_view(template_name = "jugos/actualizar.html"), name='actualizar'), 
 
# La ruta 'eliminar' que usaremos para eliminar un jugo o registro de la Base de Datos 
path('jugos/eliminar/<int:pk>', JugoEliminar.as_view(), name='eliminar'),
```
Siempre debemos pasarle a estas 3 rutas el id del registro o jugo con <int:pk> en donde int es integer y pk es primary key, ya que de esta manera Django puede saber cual es el registro que debe de leer, actualizar y eliminar de la Base de Datos.

A continuación el código completo del archivo urls.py:
```

"""cruddjango4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [ 
    
    path('admin/', admin.site.urls), 

    # La ruta 'leer' en donde listamos todos los registros o jugos de la Base de Datos
    path('jugos/', JugosListado.as_view(template_name = "jugos/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un jugo o registro 
    path('jugos/detalle/<int:pk>', JugoDetalle.as_view(template_name = "jugos/detalles.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo jugo o registro  
    path('jugos/crear', JugoCrear.as_view(template_name = "jugos/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un jugo o registro de la Base de Datos 
    path('jugos/editar/<int:pk>', JugoActualizar.as_view(template_name = "jugos/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un jugo o registro de la Base de Datos 
    path('jugos/eliminar/<int:pk>', JugoEliminar.as_view(), name='eliminar'), 

]

```

Ahora vamos a organizar los templates para el sistema CRUD.

## Templates

En el archivo urls.py que configuré anteriormente, podemos ver que cada ruta está llamando a un archivo HTML con la vista correspondiente que debe de mostrar dicha ruta, tenemos que crear un directorio llamado templates en donde crearemos 4 archivos HTML que son actualizar.html, crear.html, detalles.html y index.html 

El directorio templates no viene con Django Framework o se crea automáticamente, este directorio lo debemos crear manualmente dentro del directorio de nuestra aplicación jugos y dentro del directorio templates debo crear otro directorio llamado jugos, es decir la ruta quedaria como cruddjango4 > jugos > templates >jugos

```

/cruddjango4 
    ├── /cruddjango4 
    ├── /mientornovirtual 
    ├── /jugos 
        ├── /__pycache__
        ├── /migrations
        ├── /static
        ├── /templates 
            ├── /jugos  
                ├── actualizar.html // Creamos este archivo 
                ├── crear.html // Creamos este archivo 
                ├── detalles.html // Creamos este archivo 
                ├── index.html // Creamos este archivo 
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        ├── views.py 
    ├── db.sqlite3
    ├── manage.py 
├── /miev 

```
## Instalación y Configuración de Paquetes

Instalaré y configuraré un par de paquetes para mi proyecto:

Bootstrap 5
El Framework Bootstrap 5 nos permite crear interfaces HTML de manera rápida, asi nos enfocamos solamente en la lógica de la aplicación. Voy a instalar la librería django-bootstrap5 ejecutando el siguiente comando, esta librería nos instala Bootstrap 5 dentro del Framework Django:

```
# Comando para instalar el paquete 'django-bootstrap5' 
pip install django-bootstrap5 
```

## Django Widget Tweaks
Ahora instalaré el paquete django-widget-tweaks que me permite renderizar y gestionar los campos de los formularios de manera ágil, ejecuto el siguiente comando para instalarlo:
```
# Comando para instalar el paquete 'django-widget-tweaks' 
pip install django-widget-tweaks 
```
Igualmente, para más información puedes visitar el enlace del paquete.

Para que los paquetes instalados anteriormente funcionen en mi proyecto, debo de instanciarlos dentro del archivo settings.py que se encuentra en cruddjango4 > cruddjango4 > settings.py 
```
/cruddjango4 
    ├── /cruddjango4 
        ├── __init__.py 
        ├── asgi.py 
        ├── settings.py // Abro este archivo 
        ├── urls.py 
        ├── wsgi.py 
    ├── /jugos 
    ├── db.sqlite3
    ├── manage.py 
├── /miev 
```
Abro el archivo settings.py y dentro de el instancio el paquete django-bootstrap5 y django-widget-tweaks en la sección INSTALLED_APPS = []:

```

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jugos', # Registramos la app 'jugos' 
    'django_bootstrap5', # Registramos Bootstrap 5 (Este comentario es para explicación, debes de eliminarlo para probar la aplicación, si no te va a dar error)
    'widget_tweaks', #Registramos widget_tweaks (Este comentario es para explicación, debes de eliminarlo para probar la aplicación, si no te va a dar error)
]

```
Bien, hasta aquí hemos creado las rutas, configurado el directorio templates para los archivos HTML e instalado los paquetes que necesitaré para el sistema CRUD.
## Vistas HTML con Bootstrap 5
En la vista principal voy a mostrar una tabla HTML en donde se listarán los registros o jugos desde la base de datos, colocaré una tabla HTML de Bootstrap 5 con las columnas Nombre, Precio, Stock, Imagen y Acciones.

Dentro de la columna Acciones colocaré 3 botones que son Ver, Editar y Eliminar para cada registro o jugo.

Para poder crear las vistas HTML debemos de instanciar la librería o core de Bootstrap 5 junto a su archivo de estilos CSS, todo esto debemos hacerlo en cada archivo HTML de nuestro Sistema CRUD, lo colocamos entre las etiquetas <head></head> 

```

<head>

    {# Cargamos la librería #}
    {% load django_bootstrap5 %} 
 
    {# CSS Bootstrap #}
    {% bootstrap_css %} 

</head>

```
Ahora defino la configuración de la carpeta STATIC_URL en nuestro archivo settings.py
```

# Esta configuración se encuentra dentro del archivo settings.py 
STATIC_URL = '/static/'
```

Por medio de STATIC_URL le decimos a Django que usaremos la carpeta /static/ para almacenar nuestros archivos CSS, JS y las imágenes de cada registro o jugo que subamos a nuestra Base de Datos. 

En el archivo HTML colocamos entre las etiquetas <head></head> la configuración de STATIC_ROOT, lo puedes colocar debajo de la llamada que hicimos al core y archivo CSS de Bootstrap 5: 
```

<head>

    {# Cargamos la librería #} 
    {% load django_bootstrap5 %} 

    {# CSS Bootstrap #} 
    {% bootstrap_css %} </head>

    {# Archivos #}
    {% load static %} <!-- STATIC_URL -->

</head>

```
Ahora pasemos a crear las vistas HTML con Bootstrap 5 para las operaciones CRUD.

## Listar Jugos (Página Principal)

Comenzaré listando los jugos en una tabla HTML con Bootstrap 5, abre el archivo index.html y agrega lo siguiente: 

```

<table class="table table-striped table-hover">
  <thead>
    <tr>
      <th width="35%">Nombre</th>
      <th>Precio</th>
      <th>Stock</th>
      <th>Imagen</th>
      <th>Acciones</th>
    </tr>
  </thead>
  <tbody>
  
  <!-- Recorremos los objetos o registros que tenemos en nuestra tabla 'jugos' y los listamos -->
  {% for jugo in object_list %}
    <tr>
      <td>{{ jugo.nombre }}</td>
      <td>{{ jugo.precio }}</td>
      <td>{{ jugo.stock }}</td>
      <td><img src="{% static 'uploads/'%}{{jugo.img}}" alt="{{jugo.nombre}}" class="img-fluid" width="7%"></td>
      <td>

        <!-- Usaremos un formulario que realizará la tarea de eliminar un registro o jugo desde la misma tabla HTML -->                        
        <form method="POST" action="eliminar/{{jugo.id}}">
          {% csrf_token %}
          <div class="btn-group">

            <!-- Creamos 3 botones que son ver, Editar y Eliminar, nos sirven para gestionar nuestros registros o jugos -->
            <a href="detalle/{{jugo.id}}" title="Ver" type="button" class="btn btn-success">Ver </a>
            <a href="editar/{{jugo.id}}" title="Editar" type="button" class="btn btn-primary">Editar </a>
            <button class="btn btn-danger" onclick="return eliminar();" type="submit">
              Eliminar
            </button>
          </div>
        </form>

      </td>
    </tr>
  {% endfor %}

  </tbody>
</table>

```
Entonces con esto obtenemos nuestra vista principal (index.html) con el listado respectivo de los jugos o registros.
Y cada ves que en la tabla HTML aparece un registro o jugo nuevo, el sistema le asigna una tira de botones que son Ver, Editar y Eliminar.

## Crear (Create)

Esta vista servirá para la creación de un nuevo registro o jugo, abro el archivo crear.html el cual lo cree en la parte 3 de este tutorial, este archivo se encuentra dentro de la carpeta templates y le agrego el siguiente formulario: 

```

<form method="post" enctype="multipart/form-data">
  
  # Pasamos el 'csrf_token' de seguridad para poder crear un nuevo registro
  {% csrf_token %}
  
  <!-- {{ form.as_p }} -->
  <div class="form-group">
    <label for="nombre" class="txt_negrita">Nombre</label>
    {{ form.nombre|add_class:"form-control" }} <!-- Usamos la librería 'widget_tweaks' para crear esta caja de texto -->
  </div>
  <div class="form-group">
    <label for="precio" class="txt_negrita">Precio</label>
    {{ form.precio|add_class:"form-control" }} <!-- Usamos la librería 'widget_tweaks' para crear esta caja de texto --> 
  </div>
  <div class="form-group">
    <label for="stock" class="txt_negrita">Stock</label>
    {{ form.stock|add_class:"form-control" }} <!-- Usamos la librería 'widget_tweaks' para crear esta caja de texto -->
  </div>
  <div class="form-group">
    <label for="img" class="txt_negrita">Imagen</label>
    {{ form.img|add_class:"form-control mb-3" }} <!-- Usamos la librería 'widget_tweaks' para crear esta caja de texto -->
  </div>
  
  <button type="submit" class="btn btn-primary">Aceptar</button>
  <a href="./" type="submit" class="btn btn-primary">Cancelar</a>

</form>

```
Puedes ver en el código del archivo crear.html que estamos usando la librería widget_tweaks que instale en la Parte 4 de este  tutorial, esta librería nos permite gestionar nuestros formularios creados mediante Vistas Genéricas de Django.

Bueno con esto tenemos nuestra vista crear.html con el formulario para ingresar un nuevo jugo o registro:

## Leer (Read)
En esta vista vamos a mostrar los detalles de un archivo independientemente cada ves que el usuario haga clic en el botón Ver que se encuentra en la columna Acciones al lado de un determinado registro en la tabla HTML del archivo index.html

Entonces agrego el siguiente código HTML al archivo detalles.html que se encuentra en la carpeta templates, con este código imprimimos los objetos o datos con la información de un registro específico:

```

<h4>Detalles</h4>

<p><span class="txt_negrita">Nombre:</span> <br> {{object.nombre}}</p>
<p><span class="txt_negrita">Precio:</span> <br> {{object.precio}}</p>
<p><span class="txt_negrita">Stock:</span> <br> {{object.stock}}</p>
<p><span class="txt_negrita">Imagen:</span> <br> <img src="{% static 'uploads/'%}{{object.img}}" alt="{{object.nombre}}" class="img-fluid"> </p>
<p><span class="txt_negrita">Creado:</span> <br> {{object.created_at}}</p>
<p><span class="txt_negrita">Actualizado:</span> <br> {{object.updated_at}}</p>

<!-- Botón para volver a la vista principal (Home) -->
<a href="../" type="submit" class="btn btn-primary">Volver</a>

```
Django envía el id del registro al archivo o template llamado detalles.html para mostrar los detalles de dicho registro, el envío de este id lo hace por la ruta jugos/detalle/<int:pk>

```

path('jugos/detalle/<int:pk>', JugoDetalle.as_view(template_name = "jugos/detalles.html"), name='detalles'),

```

Esta ruta la definimos anteriormente en la Parte 4 de este tutorial, específicamente dentro del archivo urls.py

Con este tenemos nuestra vista Leer con los datos de un registro determinado:

## Actualizar (Update)

En esta vista colocaré un formulario HTML para poder editar un registro determinado, dentro de cada elemento Django colocaremos los valores específicos de un registro o jugo.

Abro el archivo actualizar.html que se encuentra en la carpeta templates y agrego el siguiente código HTML
```

<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  
  <!-- {{ form.as_p }} -->
  <div class="form-group">
    <label for="nombre" class="txt_negrita">Nombre</label>
    {{ form.nombre|add_class:"form-control" }} <!-- Usamos la librería 'widget_tweaks' para crear esta caja de texto -->
  </div>
  <div class="form-group">
    <label for="precio" class="txt_negrita">Precio</label>
    {{ form.precio|add_class:"form-control" }}
  </div>
  <div class="form-group">
    <label for="stock" class="txt_negrita">Stock</label>
    {{ form.stock|add_class:"form-control" }}
  </div>
  <div class="form-group">
    <label for="img" class="txt_negrita">Imagen</label>
    {{ form.img|add_class:"form-control mb-3" }}
    <p class="txt_negrita">Imagen Actual:</p>
    <img src="{% static 'uploads/'%}{{object.img}}" class="img-fluid" alt="{{object.nombre}}">
  </div>

  <button type="submit" class="btn btn-primary">Aceptar</button>
  <a href="../" type="submit" class="btn btn-primary">Volver</a>

</form>

```
En la siguiente ruta para actualizar, le paso el id del registro que vamos a Editar o actualizar:  

```

path('jugos/editar/<int:pk>', JugoActualizar.as_view(template_name = "jugos/actualizar.html"), name='actualizar'),

```
Mediante la ruta anterior, Django nos envía al archivo actualizar.html los datos de un determinado registro y los coloca dentro del formulario listos para poder ser editados: 

Por último trabajaremos en la vista HTML Eliminar, pero más que una vista es una función o tarea del sistema CRUD, veamosla mejor a continuación. 

## Eliminar (Delete)

En esta vista vamos a usar el archivo index.html que se encuentra dentro de la carpeta templates, en este archivo estamos listando todos los registros o jugos de la Base de Datos.

Dentro de la columna Acciones puedes ver en el código que he colocado un formulario, este formulario solo nos va servir para ejecutar la eliminación de un registro desde la misma tabla HTML donde listamos los registros:
```

<table class="table table-striped table-hover">
  <thead>
    <tr>
      <th width="35%">Nombre</th>
      <th>Precio</th>
      <th>Stock</th>
      <th>Imagen</th>
      <th>Acciones</th>
    </tr>
  </thead>
  <tbody>  

  {% for jugo in object_list %}
    <tr>
      <td>{{ jugo.nombre }}</td>
      <td>{{ jugo.precio }}</td>
      <td>{{ jugo.stock }}</td>
      <td><img src="{% static 'uploads/'%}{{jugo.img}}" alt="{{jugo.nombre}}" class="img-fluid" width="7%"></td>
      <td>

        <!-- Usaremos un formulario que realizará la tarea de eliminar un registro o jugo desde la misma tabla HTML -->                        
        <form method="POST" action="eliminar/{{jugo.id}}">
          {% csrf_token %}
          <div class="btn-group">
            
            <a href="detalle/{{jugo.id}}" title="Ver" type="button" class="btn btn-success">Ver </a>
            <a href="editar/{{jugo.id}}" title="Editar" type="button" class="btn btn-primary">Editar </a>
            
            <!-- Este botón ejecuta el formulario para eliminar un registro o jugo en la Base de datos -->
            <button class="btn btn-danger" onclick="return eliminar();" type="submit">
              Eliminar
            </button>

          </div>
        </form>

      </td>
    </tr>
  {% endfor %}

  </tbody>
</table>

```

La idea es hacer la eliminación de los registros desde la misma página, no sería muy estético eliminar el registro en una nueva página HTML, salvo que tu proyecto lo requiera.

Entonces por seguridad antes de eliminar un registro, vamos a consultar al usuario si desea eliminar un registro, dentro de nuestro botón para enviar el formulario llamamos a la función Javascript eliminar();

```

<button class="btn btn-danger" onclick="return eliminar();" type="submit">
  Eliminar
</button> 

```
Cuando el usuario hace clic en el botón se muestra una alerta con el mensaje Eliminar Producto ?

La función eliminar(); la he creado con Javascript y la colocamos al final antes de cerrar la etiqueta </body> de nuestro archivo HTML llamado index.html

```

    <script type="text/javascript">
      function eliminar() {
        var x = confirm("Eliminar Producto ?");
        if (x)
          return true;
        else
          return false;
      }
    </script>
    
  </body>
</html>

```
Bien, cuando el usuario haga clic en el botón Eliminar de alguno de los registros que se encuentran en la columna Acciones de la tabla HTML, le lanzamos la alerta para que confirme la eliminación del registro:  

De esta manera impedimos que el usuario borre por error alguno de sus registros. 

## Mensajes

En el archivo index.html van a recaer todos los mensajes de las operaciones Crear, Eliminar y Actualizar, es decir después de Insertar, Eliminar o Actualizar un registro o jugo de la Base de Datos, mostramos un mensaje para confirmar que dicha operación ha sido realizada Correctamente.

Abro el archivo index.html que se encuentra en la carpeta templates y agrega el siguiente código:

```

{% if messages %}
  <ul class="messages list-group mb-3">
    {% for message in messages %}
    <li{% if message.tags %} class="{{ message.tags }} list-group-item list-group-item-primary"{% endif %}>{{ message }}</li>
    {% endfor %}
  </ul>
{% endif %}

```

Por ejemplo cuando el usuario Edite un registro o jugo, se le va mostrar un mensaje diciendo que la operación ha sido realizada correctamente, este mensaje también le va aparecer cuando Crea o Elimina un registro: 

Ahora veremos la carpeta uploads, una carpeta importante para la subida de las imagenes.

## La carpeta uploads

Debemos de crear una carpeta para las imágenes de cada Registro que el usuario crea, yo le pondré de nombre uploads a esta carpeta y la creamos dentro de la carpeta jugos > static > uploads

```

/cruddjango4 
    ├── /cruddjango4 
    ├── /jugos 
        ├── /__pycache__
        ├── /migrations
        ├── /static
        ├── /templates 
            ├── /css 
            ├── /uploads # Creo esta carpeta 
                ├── jn.jpg
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        ├── views.py 
    ├── db.sqlite3
    ├── manage.py 
├── /miev 

```
Con eso ya tenemos finalizado nuestro sistema CRUD.

## Configuraciones Adicionales

Por favor te recomiendo revisar el archivo settings.py alojado en el Repositorio GitHub de este proyecto en donde esta toda la configuración que he realizado, pero debo destacar las siguientes configuraciones (He colocado comentarios para explicar que hace cada parte del código): 


```

# La URL para los archivos Estáticos (CSS, JS, Imágenes, etc.)
STATIC_URL = '/static/' 

# Las rutas para las imágenes de cada registro o jugo  
MEDIA_URL = '/jugos/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'jugos/static/uploads')

# Activamos 'CookieStorage' que nos permite enviar los mensajes de respuesta al Crear, Eliminar y Actualizar un registro
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

```
