# Generated by Django 2.1.8 on 2021-11-10 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0031_auto_20211110_1525'),
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
        migrations.AlterField(
            model_name='theadd',
            name='subcategories',
            field=models.ManyToManyField(blank=True, related_name='subcategories', to='mainApp.category'),
        ),
    ]
