# Generated by Django 5.0.2 on 2024-04-07 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='listinghouseamenities',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='listinghousearea',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='listingspaceoverview',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='rentalconditions',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='rulesandpreferences',
            name='seller',
        ),
    ]
