# Generated by Django 4.0.4 on 2022-06-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_tag_meta_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='keywords',
            field=models.CharField(blank=True, max_length=100, verbose_name='Meta keywords tag'),
        ),
    ]