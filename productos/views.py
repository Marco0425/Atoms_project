from itertools import product
from multiprocessing import context
from sqlite3 import PrepareProtocol

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from productos.models import Prodcutos


def index(request):
    return HttpResponse("Hello, world. Estas en la url de productos.")



@csrf_exempt
def reg_data_new(request, *args, **kwargs):
    js = json.loads(request.body)
    # =============== Inicio de validaciones de campos ====================================
    prod_tag = js['productos']['tag_product']
    if len(prod_tag.split(',')) >= 26: # no deja registrar mas de 25 Tags para este campo
        context = {'Menaje':'El numero de TAGS supera los registros aceptados'}
    elif Prodcutos.objects.filter(SKU=js['productos']['SKU']): # No deja hacer el registro si ya existe ese SKU y actualiza el existente
        update_reg = Prodcutos.objects.get(SKU=js['productos']['SKU'])
        update_reg.product_name = js['productos']['product_name']
        update_reg.tag_product = js['productos']['tag_product']
        update_reg.cost = js['productos']['cost']
        update_reg.status = js['productos']['status']
        update_reg.save()


        context = {'Menaje':'Registro actualizado'}
    elif not js['productos']['status'] in ['active','archived','draft']: # Evita que se registre si tiene un estatus diferente a active, archived o draft
        context = {'Menaje':'Ese estatus no esta permitido para el registro'}
    # ====================== Fin de validaciones de campos ================================
    else:
    # ====================== Inicio de Insert en tabla Prodcutos ================================
        Prodcutos.objects.create(product_name=js['productos']['product_name'], # Crea el objeto para ser insertado en la base de datos
                            SKU=js['productos']['SKU'],
                            tag_product=js['productos']['tag_product'],
                            cost=js['productos']['cost'],
                            status=js['productos']['status'])

        context = {'Menaje':'Succes'}
    # ====================== Inicio de Insert en tabla Prodcutos ================================
    return JsonResponse(context)

def listado_productos(request):
    Prod = list(Prodcutos.objects.all())
    context = {
        'Titulo':'Productos',
        'Productos':Prod,
    }

    template = 'productos/index.html'
    return render(request, template, context)