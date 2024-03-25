<<<<<<< HEAD
# Generated by Django 5.0.3 on 2024-03-15 14:33
=======
# Generated by Django 5.0.2 on 2024-03-20 19:03
>>>>>>> 61f1a9b110687a4403a152198c8a3ee8b4f2065b

import django.db.models.deletion
import main.utils
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListingHouseAmenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=24, verbose_name='Bed')),
                ('wifi', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=24, verbose_name='Wifi')),
                ('desk', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=24, verbose_name='Desk')),
                ('living_room_furnished', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=24, verbose_name='Living Room Furnished')),
            ],
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
            ],
        ),
        migrations.CreateModel(
            name='ListingSpaceOverview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_size', models.CharField(max_length=24)),
                ('house_mate_no', models.CharField(max_length=24)),
                ('bedroom_size', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=24, verbose_name='Bedroom Size')),
                ('bedroom_furnished', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='RentalConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.CharField(choices=[('daily', 'Daily'), ('monthly', 'Monthly'), ('fortnight', 'Fortnight')], max_length=24, verbose_name='Contract Type')),
                ('cancellation', models.CharField(choices=[('strict cancellation', 'Strict Cancellation'), ('flexible cancellation', 'Flexible Cancellation')], max_length=24, verbose_name='Cancellation Option')),
                ('price', models.CharField(choices=[('basic price', 'Basic Price'), ('advanced price', 'Advanced Price')], max_length=24, verbose_name='Price')),
                ('utility_costs', models.CharField(max_length=24)),
            ],
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
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.PositiveSmallIntegerField()),
                ('available_start', models.DateTimeField(null=True)),
                ('available_end', models.DateTimeField(null=True)),
                ('image', models.ImageField(upload_to=main.utils.user_listing_path)),
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
            name='HouseArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Listing_house_area', to='main.listing')),
                ('house_area', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='house_area', to='main.listinghousearea')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateTimeField(default=None)),
                ('check_out_date', models.DateTimeField(default=None)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.listing')),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_amenities', to='main.listing')),
                ('amenity_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='amenity_type', to='main.listinghouseamenities')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='amenities',
            field=models.ManyToManyField(through='main.Amenity', to='main.listinghouseamenities'),
        ),
        migrations.AddField(
            model_name='listing',
            name='listing_house_area',
            field=models.ManyToManyField(through='main.HouseArea', to='main.listinghousearea'),
        ),
        migrations.CreateModel(
            name='ListingSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_spaces', to='main.listing')),
                ('space_overview', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='space_overview', to='main.listingspaceoverview')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='listing_space_overview',
            field=models.ManyToManyField(through='main.ListingSpace', to='main.listingspaceoverview'),
        ),
        migrations.CreateModel(
            name='RentalCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rental_conditions', to='main.listing')),
                ('rental_conditions', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='rental_conditions', to='main.rentalconditions')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='rental_condtion',
            field=models.ManyToManyField(through='main.RentalCondition', to='main.rentalconditions'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('rating', models.PositiveSmallIntegerField()),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.listing')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Listing_rules', to='main.listing')),
                ('rules_and', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='rules_and_preferences', to='main.rulesandpreferences')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='rules_and_preferences',
            field=models.ManyToManyField(through='main.Rules', to='main.rulesandpreferences'),
        ),
    ]
