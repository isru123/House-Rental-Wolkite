# Generated by Django 5.0.2 on 2024-02-28 18:39

import main.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_listingspaceoverview'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListAmenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed', models.CharField(max_length=25)),
                ('wifi', models.CharField(max_length=25)),
                ('desk', models.CharField(max_length=25)),
                ('living_room_furnished', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ListArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitchen', models.CharField(max_length=25)),
                ('toilet', models.CharField(max_length=25)),
                ('bathroom', models.CharField(max_length=25)),
                ('living_room', models.CharField(max_length=25)),
                ('garden', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ListRentalConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_contract', models.CharField(max_length=25)),
                ('fortnight_contract', models.CharField(max_length=25)),
                ('monthly_contract', models.CharField(max_length=25)),
                ('strict_cancellation', models.CharField(max_length=25)),
                ('flexible_cancellation', models.CharField(max_length=25)),
                ('basic_price', models.CharField(max_length=25)),
                ('advanced_price', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ListRulesPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=25)),
                ('min_age', models.CharField(max_length=25)),
                ('max_age', models.CharField(max_length=25)),
                ('any_tenant', models.CharField(max_length=25)),
                ('student_tenant', models.CharField(max_length=25)),
                ('working_pro_tenant', models.CharField(max_length=25)),
                ('proof_of_identity', models.CharField(max_length=25)),
                ('proof_of_occupation', models.CharField(max_length=25)),
                ('proof_of_income', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ListSpaceOverview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_size', models.CharField(max_length=25)),
                ('house_mate_no', models.CharField(max_length=25)),
                ('bedroom_size', models.CharField(max_length=25)),
                ('bedroom_furnished', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(upload_to=main.utils.user_listing_path),
        ),
    ]
