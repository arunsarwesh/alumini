# Generated by Django 5.1.6 on 2025-03-21 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_album_cover_image_alter_albumimage_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='isjob',
            field=models.BooleanField(default=False),
        ),
    ]
