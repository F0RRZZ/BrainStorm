# Generated by Django 3.2.16 on 2023-04-06 11:57

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(help_text='Имя пользователя', max_length=100, verbose_name='username')),
                ('bio', models.TextField(help_text='О себе', max_length=1000, verbose_name='bio')),
                ('first_name', models.CharField(blank=True, help_text='Имя', max_length=100, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, help_text='Фамилия', max_length=100, null=True, verbose_name='last name')),
                ('email', models.EmailField(help_text='Электронная почта', max_length=254, unique=True, verbose_name='email address')),
                ('normalized_email', users.models.NormalizedEmailField(help_text='Нормализованная электронная почта', max_length=254, unique=True, verbose_name='normalized email address')),
                ('date_joined', models.DateTimeField(auto_now=True, help_text='Дата регистрации', verbose_name='date joined')),
                ('is_active', models.BooleanField(default=False, help_text='Активен', verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, help_text='Персонал', verbose_name='staff')),
                ('is_superuser', models.BooleanField(default=False, help_text='Суперпользователь', verbose_name='superuser')),
                ('image', models.ImageField(blank=True, help_text='Аватарка', null=True, upload_to=users.models.User.get_image_filename, verbose_name='profile picture')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
        ),
    ]