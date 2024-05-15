# Generated by Django 4.2.6 on 2024-05-12 11:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_upload_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
