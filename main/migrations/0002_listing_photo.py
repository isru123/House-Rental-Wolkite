# Generated by Django 4.2.6 on 2024-04-16 15:37

from django.db import migrations, models
import main.utils


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='photo',
            field=models.ImageField(default='', upload_to=main.utils.user_listing_path),
            preserve_default=False,
        ),
    ]
