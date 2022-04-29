# Generated by Django 4.0.4 on 2022-04-29 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_techskill_alter_education_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='education',
            name='level',
            field=models.CharField(blank=True, max_length=20, verbose_name='Education Level'),
        ),
        migrations.AlterField(
            model_name='job',
            name='company_details',
            field=models.TextField(blank=True, verbose_name='Company Description'),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(blank=True, max_length=50, verbose_name='Location/Remote'),
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.TextField(blank=True, verbose_name='Job Description'),
        ),
        migrations.AlterField(
            model_name='techskill',
            name='certs',
            field=models.CharField(blank=True, max_length=100, verbose_name='Certification(s)'),
        ),
        migrations.AlterField(
            model_name='techskill',
            name='details',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
    ]
