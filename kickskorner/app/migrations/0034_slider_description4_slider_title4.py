# Generated by Django 4.2.1 on 2023-05-21 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_slider_image4'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='description4',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='slider',
            name='title4',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
