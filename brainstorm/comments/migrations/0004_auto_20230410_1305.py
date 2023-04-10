# Generated by Django 3.2.16 on 2023-04-10 13:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_author'),
        ('comments', '0003_auto_20230410_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 4, 10, 13, 5, 12, 390756), verbose_name='дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='дата изменения'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(help_text='Какому проекту принадлежит комментарий', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='projects.project', verbose_name='проект'),
        ),
    ]