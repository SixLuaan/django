# Generated by Django 4.0.4 on 2022-05-05 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_product_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='review_times',
            field=models.IntegerField(default=0),
        ),
    ]