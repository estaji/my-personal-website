# Generated by Django 4.0.4 on 2022-06-30 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_tag_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='robots',
            field=models.CharField(blank=True, max_length=60, verbose_name='Meta robots tag'),
        ),
    ]