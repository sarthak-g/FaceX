# Generated by Django 2.1.1 on 2019-02-03 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
