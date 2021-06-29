# Generated by Django 3.2.3 on 2021-06-27 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20210626_0829'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['order'], 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='tema',
            options={'ordering': ['order']},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='ordering',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='ordering',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='tema',
            old_name='ordering',
            new_name='order',
        ),
    ]