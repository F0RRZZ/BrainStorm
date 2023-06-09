# Generated by Django 3.2.16 on 2023-04-19 18:06

import ckeditor.fields
import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '0005_auto_20230419_2106'),
        ('projects', '0012_auto_20230418_1855'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagesgallery',
            options={'verbose_name': 'галерея', 'verbose_name_plural': 'галереи'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'project', 'verbose_name_plural': 'projects'},
        ),
        migrations.AlterField(
            model_name='imagesgallery',
            name='image',
            field=models.ImageField(upload_to=core.models.directory_path, verbose_name='preview'),
        ),
        migrations.AlterField(
            model_name='imagesgallery',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_gallery', to='projects.project'),
        ),
        migrations.AlterField(
            model_name='preview',
            name='image',
            field=models.ImageField(upload_to=core.models.directory_path, verbose_name='preview'),
        ),
        migrations.AlterField(
            model_name='preview',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preview', to='projects.project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='collaborators',
            field=models.ManyToManyField(related_name='colleagues', to=settings.AUTH_USER_MODEL, verbose_name='collaborators'),
        ),
        migrations.AlterField(
            model_name='project',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creation_date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='full_description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='in_archive',
            field=models.BooleanField(default=False, verbose_name='in_archive'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=150, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='project',
            name='published',
            field=models.BooleanField(default=True, verbose_name='published'),
        ),
        migrations.AlterField(
            model_name='project',
            name='short_description',
            field=ckeditor.fields.RichTextField(verbose_name='short_description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('idea', 'idea'), ('development', 'in_develop'), ('ended', 'ended')], default='idea', max_length=20, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(help_text='5_tags_maximum__lowercase', related_name='projects', to='tags.Tag', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='project',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='update_date'),
        ),
    ]
