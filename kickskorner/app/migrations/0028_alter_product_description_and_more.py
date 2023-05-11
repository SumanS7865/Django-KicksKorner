# Generated by Django 4.1.7 on 2023-05-11 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_alter_product_discounted_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_detail_ribbon',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ribbon',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=500, unique=True),
        ),
    ]