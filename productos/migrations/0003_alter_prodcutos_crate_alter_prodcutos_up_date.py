# Generated by Django 4.1 on 2022-08-18 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_prodcutos_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodcutos',
            name='crate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='prodcutos',
            name='up_date',
            field=models.DateTimeField(),
        ),
    ]