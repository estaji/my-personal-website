# Generated by Django 4.0.4 on 2022-04-30 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jumbotron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greeting', models.CharField(max_length=50, verbose_name='Welcome Message')),
                ('title', models.CharField(max_length=50, verbose_name='Title/Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('picture', models.ImageField(upload_to='jumbotron_picture/', verbose_name='Picture/Avatar')),
            ],
        ),
    ]