# Generated by Django 2.1.8 on 2021-09-02 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_auto_20210831_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='region',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
    ]
