# Generated by Django 4.2.6 on 2024-05-09 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_upload_accepted_upload_status_alter_upload_document_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='accepted',
            field=models.CharField(choices=[('Reject', 'Reject'), ('Accept', 'Accept')], default='Pending', max_length=10),
        ),
    ]
