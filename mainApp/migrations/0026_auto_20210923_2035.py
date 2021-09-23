# Generated by Django 2.1.8 on 2021-09-23 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0025_auto_20210923_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='theadd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='messageTheadd', to='mainApp.theadd'),
        ),
        migrations.AlterField(
            model_name='role',
            name='permissiongeneral',
            field=models.ManyToManyField(to='mainApp.permissiongeneral'),
        ),
        migrations.AlterField(
            model_name='theadd',
            name='images',
            field=models.ManyToManyField(to='mainApp.attachmenttranscript'),
        ),
    ]
