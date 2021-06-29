# Generated by Django 3.2.3 on 2021-06-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_auto_20210628_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='ordering',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, default='name', null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tema',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
