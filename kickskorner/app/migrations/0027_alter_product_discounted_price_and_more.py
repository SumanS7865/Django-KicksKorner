# Generated by Django 4.1.7 on 2023-05-10 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_product_image3_alter_product_image4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.BigIntegerField(),
        ),
    ]