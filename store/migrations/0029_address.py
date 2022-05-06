# Generated by Django 4.0.4 on 2022-05-06 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_shippingaddress_name_shippingaddress_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300, null=True)),
                ('name', models.CharField(max_length=300, null=True)),
                ('phone', models.CharField(max_length=300, null=True)),
                ('time', models.DateTimeField()),
                ('city', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]