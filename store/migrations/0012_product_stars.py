# Generated by Django 4.0.4 on 2022-05-05 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_blog_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stars',
            field=models.IntegerField(default=0),
        ),
    ]