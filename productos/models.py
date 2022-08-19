from email.policy import default
from django.db import models


class Prodcutos(models.Model):

    choices_status = (
        ("active","active"),
        ("archived","archived"),
        ("draft","draft"),
    )
    product_name  = models.CharField(max_length=50) # string
    SKU = models.CharField(max_length=50, unique = True) # string - campo unico 
    image = models.ImageField(upload_to='productos', default=None, null=True) # lista de datos en base64 
    tag_product = models.CharField(max_length=50) # Un string con palabras separadas por comas - máximo 25 tags son permitidos
    cost = models.IntegerField()# numeric
    status = models.CharField(max_length=10, choices = choices_status)# string - puede recibir solamente: active, archived o draft
    tallas = models.CharField(max_length=50) # Un string de números separados por comas - sin límite de tallas, son permitidas tallasnegativas
    crate = models.DateTimeField(auto_now_add = True) # campo no incluido en el json enviado
    up_date = models.DateTimeField(auto_now = True)# campo no incluido en el json enviado