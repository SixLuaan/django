# Generated by Django 4.0.4 on 2022-05-06 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(null=True),
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]