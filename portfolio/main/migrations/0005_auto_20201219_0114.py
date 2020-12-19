# Generated by Django 3.1.4 on 2020-12-18 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_headfoot_photo_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(blank=True, null=True, upload_to='')),
                ('photo_class', models.CharField(blank=True, max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Gallery Item',
                'verbose_name_plural': 'Gallery Items',
            },
        ),
        migrations.RemoveField(
            model_name='headfoot',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='headfoot',
            name='photo_class',
        ),
    ]