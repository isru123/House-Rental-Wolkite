# Generated by Django 4.2.6 on 2024-05-13 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_remove_listing_available_end_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rulesandpreferences',
            name='proof',
        ),
        migrations.AlterField(
            model_name='listingspaceoverview',
            name='house_size',
            field=models.CharField(max_length=24, verbose_name='House Size in m square'),
        ),
    ]