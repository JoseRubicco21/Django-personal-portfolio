# Generated by Django 4.2.16 on 2024-11-13 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='static/'),
        ),
    ]