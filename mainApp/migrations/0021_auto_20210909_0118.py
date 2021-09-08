# Generated by Django 2.1.8 on 2021-09-08 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0020_theadd_featureaddnumber'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='theadd',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='role',
            name='permissionGeneral',
        ),
        migrations.AddField(
            model_name='role',
            name='permissiongeneral',
            field=models.ManyToManyField(to='mainApp.permissiongeneral'),
        ),
        migrations.AlterField(
            model_name='theadd',
            name='images',
            field=models.ManyToManyField(to='mainApp.attachmenttranscript'),
        ),
        migrations.AlterModelTable(
            name='permissiongeneral',
            table='permissiongeneral',
        ),
        migrations.AlterModelTable(
            name='theadd',
            table='theadd',
        ),
    ]
