# Generated by Django 4.1.7 on 2023-05-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_product2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product2',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
