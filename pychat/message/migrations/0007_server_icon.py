# Generated by Django 4.0.6 on 2023-12-25 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0006_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='icon',
            field=models.ImageField(default='', upload_to='server_images/'),
        ),
    ]