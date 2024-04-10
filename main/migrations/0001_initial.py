# Generated by Django 5.0.2 on 2024-04-07 08:13

import django.db.models.deletion
import django.utils.timezone
import main.utils
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_profile_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to=main.utils.user_listing_path)),
                ('image2', models.ImageField(upload_to=main.utils.user_listing_path)),
                ('image3', models.ImageField(upload_to=main.utils.user_listing_path)),
                ('image4', models.ImageField(upload_to=main.utils.user_listing_path)),
                ('image5', models.ImageField(upload_to=main.utils.user_listing_path)),
                ('description', models.CharField(max_length=255, verbose_name='Short description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('house_kind', models.CharField(choices=[('private_room', 'Private Room'), ('shared_room', 'Shared Room')], max_length=200, verbose_name='House Kind')),
                ('description', models.TextField()),
                ('price', models.PositiveSmallIntegerField()),
                ('available_start', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('available_end', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('photo', models.ImageField(upload_to=main.utils.user_listing_path)),
                ('minimum_rental_period', models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], max_length=200)),
                ('maximum_rental_period', models.CharField(choices=[('bmw', 'BMW'), ('mercedes benz', 'Mercedes Benz'), ('audi', 'Audi'), ('subaru', 'Subaru'), ('tesla', 'Tesla'), ('jaguar', 'Jaguar'), ('land rover', 'Land Rover'), ('bentley', 'Bentley'), ('bugatti', 'Bugatti'), ('ferrari', 'Ferrari'), ('lamborghini', 'Lamborghini'), ('honda', 'Honda'), ('toyota', 'Toyota'), ('chevrolet', 'Chevrolet'), ('porsche', 'Porsche')], max_length=200)),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('image', models.ManyToManyField(to='main.image')),
                ('location', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='LikedListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_date', models.DateTimeField(default=None)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.listing')),
            ],
        ),
        migrations.CreateModel(
            name='ListingHouseAmenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=24, verbose_name='Bed')),
                ('wifi', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=24, verbose_name='Wifi')),
                ('desk', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=24, verbose_name='Desk')),
                ('living_room_furnished', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=24, verbose_name='Living Room Furnished')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='amenities',
            field=models.ManyToManyField(to='main.listinghouseamenities'),
        ),
        migrations.CreateModel(
            name='ListingHouseArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitchen', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=24, verbose_name='Kitchen')),
                ('toilet', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=24, verbose_name='Toilet')),
                ('bathroom', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=24, verbose_name='Bathroom')),
                ('living_room', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=24, verbose_name='Living Room')),
                ('garden', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=24, verbose_name='Garden')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='listing_house_area',
            field=models.ManyToManyField(to='main.listinghousearea'),
        ),
        migrations.CreateModel(
            name='ListingSpaceOverview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_size', models.CharField(max_length=24)),
                ('house_mate_no', models.CharField(max_length=24)),
                ('bedroom_size', models.CharField(max_length=24, verbose_name='Bedroom Size')),
                ('bedroom_furnished', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=24)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='listing_space_overview',
            field=models.ManyToManyField(to='main.listingspaceoverview'),
        ),
        migrations.CreateModel(
            name='RentalConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.CharField(choices=[('daily', 'Daily'), ('monthly', 'Monthly'), ('fortnight', 'Fortnight')], max_length=24, verbose_name='Contract Type')),
                ('cancellation', models.CharField(choices=[('strict cancellation', 'Strict Cancellation'), ('flexible cancellation', 'Flexible Cancellation')], max_length=24, verbose_name='Cancellation Option')),
                ('price', models.CharField(choices=[('basic price', 'Basic Price'), ('advanced price', 'Advanced Price')], max_length=24, verbose_name='Price')),
                ('utility_costs', models.CharField(max_length=24)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='rental_condtion',
            field=models.ManyToManyField(to='main.rentalconditions'),
        ),
        migrations.CreateModel(
            name='RulesAndPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10, verbose_name='Gender')),
                ('minimum_age', models.CharField(choices=[('under 15', 'Under 15'), ('18', '18'), ('20', '20')], default=None, max_length=24)),
                ('maximum_age', models.CharField(choices=[('20', '20'), ('25', '25'), ('30', '30'), ('35', '35'), ('40', '40'), ('45', '45'), ('50', '50'), ('55', '55'), ('above 60', 'Above 60')], default=None, max_length=24)),
                ('tenant', models.CharField(choices=[('any ', 'Any'), ('student ', 'Student'), ('working professional', 'Working Professional')], max_length=24, verbose_name='Tenant Type')),
                ('proof', models.CharField(choices=[('proof of identity', 'Proof of Identity'), ('proof of income', 'Proof of Income'), ('proof of occupation', 'Proof of Occupation')], max_length=24, verbose_name='Proof for Tenant')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='rules_and_preferences',
            field=models.ManyToManyField(to='main.rulesandpreferences'),
        ),
    ]
