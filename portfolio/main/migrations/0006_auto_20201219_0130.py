# Generated by Django 3.1.4 on 2020-12-18 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201219_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='photo2',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='headfoot',
            name='foot_photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='headfoot',
            name='photo_class',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
