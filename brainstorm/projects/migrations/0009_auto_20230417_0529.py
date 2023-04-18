# Generated by Django 3.2.16 on 2023-04-17 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '0003_auto_20230410_2121'),
        ('projects', '0008_auto_20230416_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='project',
            name='collaborators',
            field=models.ManyToManyField(related_name='colleagues', to=settings.AUTH_USER_MODEL, verbose_name='collaborators__lowercase'),
        ),
        migrations.AlterField(
            model_name='project',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creation_date__lowercase'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='description__lowercase'),
        ),
        migrations.AlterField(
            model_name='project',
            name='in_archive',
            field=models.BooleanField(default=False, verbose_name='in_archive__lowercase'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=150, verbose_name='name__lowercase'),
        ),
        migrations.AlterField(
            model_name='project',
            name='published',
            field=models.BooleanField(default=True, verbose_name='published__lowercase'),
        ),
        migrations.AlterField(
            model_name='project',
            name='short_description',
            field=models.TextField(verbose_name='short_description__lowercase'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('idea', 'idea'), ('development', 'in_develop'), ('ended', 'ended')], default='idea', max_length=20, verbose_name='project_status__lowercase'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(related_name='projects', to='tags.Tag', verbose_name='tags__lowercase'),
        ),
        migrations.AlterField(
            model_name='project',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='update_date__lowercase'),
        ),
    ]