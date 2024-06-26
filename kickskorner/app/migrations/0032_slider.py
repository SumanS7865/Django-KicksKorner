# Generated by Django 4.2.1 on 2023-05-21 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_variation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, upload_to='photos/sliders')),
                ('image2', models.ImageField(blank=True, upload_to='photos/sliders')),
                ('image3', models.ImageField(blank=True, upload_to='photos/sliders')),
                ('title1', models.CharField(max_length=200)),
                ('title2', models.CharField(max_length=200)),
                ('title3', models.CharField(max_length=200)),
                ('description1', models.CharField(max_length=500)),
                ('description2', models.CharField(max_length=500)),
                ('description3', models.CharField(max_length=500)),
            ],
        ),
    ]
