# Generated by Django 2.1.1 on 2019-02-07 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_no', models.CharField(max_length=10)),
                ('date_of_visiting', models.CharField(max_length=11)),
                ('symptoms', models.TextField(max_length=300)),
                ('drugs', models.TextField(max_length=300)),
                ('dosage', models.TextField(max_length=300)),
                ('tests_to_be_done', models.TextField(max_length=300)),
                ('date_for_revisit', models.CharField(max_length=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('sex', models.CharField(max_length=11)),
                ('dob', models.DateField()),
                ('height_in_inches', models.IntegerField()),
                ('weight_in_kg', models.IntegerField()),
                ('phone', models.CharField(max_length=10)),
                ('marital_status', models.CharField(max_length=50)),
                ('residence', models.CharField(max_length=200)),
                ('postal_code', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('emergency_contact_first_name', models.CharField(max_length=50)),
                ('emergency_contact_last_name', models.CharField(max_length=50, null=True)),
                ('emergency_contact_relationship', models.CharField(max_length=30)),
                ('emergency_contact_phone_no', models.BigIntegerField()),
                ('taking_any_medication_currently', models.CharField(max_length=3)),
                ('medication_if_yes', models.TextField(max_length=300, null=True)),
                ('recorded_created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Records',
            },
        ),
    ]
