# Generated by Django 4.2.2 on 2023-06-22 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('about', models.CharField(max_length=255)),
                ('fblink', models.CharField(max_length=255)),
                ('twlink', models.CharField(max_length=255)),
                ('inlink', models.CharField(max_length=255)),
                ('lilink', models.CharField(max_length=255)),
                ('skills', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cpdomain', models.CharField(max_length=255)),
                ('skills', models.JSONField()),
                ('salary', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('cplink', models.CharField(max_length=255)),
                ('fblink', models.CharField(max_length=255)),
                ('twlink', models.CharField(max_length=255)),
                ('inlink', models.CharField(max_length=255)),
                ('lilink', models.CharField(max_length=255)),
                ('skills', models.JSONField()),
            ],
        ),
    ]