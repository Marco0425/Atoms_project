# Generated by Django 4.1 on 2022-08-19 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_prodcutos_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodcutos',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='productos'),
        ),
    ]
