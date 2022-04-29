# Generated by Django 4.0.4 on 2022-04-28 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Job Title')),
                ('company', models.CharField(max_length=50, verbose_name='Company Name')),
                ('logo', models.ImageField(upload_to='company_logos/', verbose_name='Company Logo')),
                ('url', models.URLField(default='https://#', max_length=50, verbose_name='Company URL')),
                ('company_details', models.TextField(verbose_name='Company Description')),
                ('start', models.DateField(verbose_name='Start Date')),
                ('end', models.DateField(null=True, verbose_name='End Date')),
                ('location', models.CharField(max_length=50, verbose_name='Location/Remote')),
                ('summary', models.TextField(verbose_name='Job Description')),
            ],
            options={
                'ordering': ['-end'],
            },
        ),
    ]
