# Generated by Django 5.1.6 on 2025-03-18 04:55

import api.models
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingSignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('college_name', models.CharField(max_length=500)),
                ('role', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('social_links', models.JSONField(blank=True, default=api.models.get_default_social_links)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='cover_pics/')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, default='+911234567890', max_length=128, region=None)),
                ('passed_out_year', models.PositiveIntegerField(blank=True, null=True)),
                ('current_work', models.CharField(blank=True, max_length=255)),
                ('previous_work', models.JSONField(blank=True, default=list)),
                ('experience', models.JSONField(blank=True, default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('approved_at', models.DateTimeField(blank=True, null=True)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SignupOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('code', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('college_name', models.CharField(max_length=500)),
                ('role', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('social_links', models.JSONField(blank=True, default=api.models.get_default_social_links)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='cover_pics/')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, default='+911234567890', max_length=128, region=None)),
                ('passed_out_year', models.PositiveIntegerField(blank=True, null=True)),
                ('current_work', models.CharField(blank=True, max_length=255)),
                ('previous_work', models.JSONField(blank=True, default=list)),
                ('experience', models.JSONField(blank=True, default=list)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='customuser_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='album_covers/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='album_images/')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.album')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('venue', models.CharField(max_length=255)),
                ('from_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_images/')),
                ('tag', models.CharField(blank=True, max_length=255)),
                ('uploaded_by', models.CharField(choices=[('Student', 'student'), ('staff', 'Staff'), ('admin', 'Admin')], default='Student', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('salary_range', models.CharField(blank=True, max_length=100)),
                ('job_type', models.CharField(blank=True, max_length=100)),
                ('views', models.PositiveIntegerField(default=0)),
                ('reaction', models.JSONField(blank=True, default=api.models.get_default_reaction)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='job_images/')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.jobs')),
            ],
        ),
        migrations.CreateModel(
            name='JobComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_comments', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.jobs')),
            ],
        ),
        migrations.CreateModel(
            name='LoginLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('successful', models.BooleanField(default=False)),
                ('browser', models.CharField(blank=True, max_length=100, null=True)),
                ('browser_version', models.CharField(blank=True, max_length=20, null=True)),
                ('device', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='login_logs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_reactions', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='api.jobs')),
            ],
            options={
                'unique_together': {('job', 'user')},
            },
        ),
    ]
