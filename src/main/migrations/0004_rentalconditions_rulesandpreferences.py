# Generated by Django 4.2.6 on 2024-02-26 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_listinghouseamenities_listinghousearea'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentalConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_contract', models.CharField(max_length=24)),
                ('fortnight_contract', models.CharField(max_length=24)),
                ('monthly_contract', models.CharField(max_length=24)),
                ('strict_cancellation', models.CharField(max_length=24)),
                ('flexible_cancellation', models.CharField(max_length=24)),
                ('basic_price', models.CharField(max_length=24)),
                ('advanced_price', models.CharField(max_length=24)),
                ('utility_costs', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='RulesAndPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=24)),
                ('minimum_age', models.CharField(max_length=24)),
                ('maximum_age', models.CharField(max_length=24)),
                ('any_tenant', models.CharField(max_length=24)),
                ('student_tenant', models.CharField(max_length=24)),
                ('professional_tenant', models.CharField(max_length=24)),
                ('proof_identity', models.CharField(max_length=24)),
                ('proof_income', models.CharField(max_length=24)),
                ('proof_occupation', models.CharField(max_length=24)),
            ],
        ),
    ]
