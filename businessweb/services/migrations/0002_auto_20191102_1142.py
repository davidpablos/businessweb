# Generated by Django 2.2.6 on 2019-11-02 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='services', verbose_name='Imagen'),
        ),
    ]