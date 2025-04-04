# Generated by Django 5.1.6 on 2025-03-27 17:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_events_uploaded_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField()),
                ('longitude', models.CharField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
