# Generated by Django 2.1.8 on 2021-08-20 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_attachmenttranscript_theadd'),
    ]

    operations = [
        migrations.AddField(
            model_name='theadd',
            name='mainImage',
            field=models.ImageField(null=True, upload_to='attachments/mainImage/'),
        ),
    ]