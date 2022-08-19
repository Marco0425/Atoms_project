from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nuevo_registro/', views.reg_data_new, name='nuevo_registro'),
    path('tabla_listado/', views.listado_productos, name='Listar_productos'),
]