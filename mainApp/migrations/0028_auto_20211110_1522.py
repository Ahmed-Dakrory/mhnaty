# Generated by Django 2.1.8 on 2021-11-10 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0027_auto_20211103_1939'),
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