# Generated by Django 2.1.8 on 2021-08-30 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_theadd_mainimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='theadd',
            name='averageRate',
            field=models.FloatField(blank=True, null=True),
        ),
    ]