# Generated by Django 4.2.6 on 2024-04-16 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_listing_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='main.listing'),
        ),
    ]