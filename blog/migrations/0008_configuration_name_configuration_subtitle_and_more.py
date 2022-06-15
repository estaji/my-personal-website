# Generated by Django 4.0.4 on 2022-06-15 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_configuration_github'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='name',
            field=models.CharField(default='Blog Name', max_length=50, verbose_name='Title in menu bar'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100, verbose_name='Sub-title in main page'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='title',
            field=models.CharField(default='Blog Title', max_length=70, verbose_name='Title in main page'),
        ),
    ]
