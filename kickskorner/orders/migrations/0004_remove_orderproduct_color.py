# Generated by Django 4.2.1 on 2023-09-03 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_tax_alter_order_city_alter_order_shipping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='color',
        ),
    ]
