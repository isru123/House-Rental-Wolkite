# Generated by Django 5.0.2 on 2024-03-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
