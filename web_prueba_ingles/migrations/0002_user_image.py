# Generated by Django 4.2.2 on 2023-06-20 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_prueba_ingles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]