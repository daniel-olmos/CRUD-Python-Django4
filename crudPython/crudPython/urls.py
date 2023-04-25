"""
URL configuration for crudPython project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from jugos.views import JugosListado, JugoDetalle, JugoCrear, JugoActualizar, JugoEliminar


urlpatterns = [
    path('admin/', admin.site.urls),

    # La ruta 'leer' en donde listamos todos los registros o jugos de la Base de Datos
    path('', JugosListado.as_view(template_name = "jugos/index.html"), name='leer'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un jugo o registro 
    path('detalle/<int:pk>', JugoDetalle.as_view(template_name = "jugos/detalles.html"), name='detalles'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo jugo o registro  
    path('crear', JugoCrear.as_view(template_name = "jugos/crear.html"), name='crear'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un jugo o registro de la Base de Datos 
    path('editar/<int:pk>', JugoActualizar.as_view(template_name = "jugos/actualizar.html"), name='actualizar'), 
    # La ruta 'eliminar' que usaremos para eliminar un jugo o registro de la Base de Datos 
    path('eliminar/<int:pk>', JugoEliminar.as_view(), name='eliminar'), 
]
