# Generated by Django 4.2.1 on 2023-09-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_staff_link'),
        ('orders', '0004_remove_orderproduct_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='variation',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='variations',
            field=models.ManyToManyField(blank=True, to='app.variation'),
        ),
    ]