# Generated by Django 5.1 on 2024-08-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]
