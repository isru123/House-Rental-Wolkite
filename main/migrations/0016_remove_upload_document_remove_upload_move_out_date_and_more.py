# Generated by Django 4.2.6 on 2024-05-12 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_upload_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='document',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='move_out_date',
        ),
        migrations.DeleteModel(
            name='Request',
        ),
    ]
