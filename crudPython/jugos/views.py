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
