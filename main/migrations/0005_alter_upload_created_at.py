# Generated by Django 4.2.6 on 2024-05-06 18:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_upload_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
