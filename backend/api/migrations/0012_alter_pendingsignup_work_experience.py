# Generated by Django 5.1.6 on 2025-04-16 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_customuser_contact_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingsignup',
            name='work_experience',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
