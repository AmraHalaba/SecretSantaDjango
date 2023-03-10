# Generated by Django 4.1.4 on 2022-12-27 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name: ')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name: ')),
                ('email', models.CharField(max_length=50, unique=True, verbose_name='Email: ')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date of Entry in DB: ')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date of Update: ')),
                ('slug', models.SlugField(blank=True, help_text='Automatically Created. ', unique=True, verbose_name='URL Snippet: ')),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
            },
        ),
    ]
