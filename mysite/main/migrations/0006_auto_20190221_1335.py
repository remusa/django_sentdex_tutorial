# Generated by Django 2.1.5 on 2019-02-21 19:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190221_1330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='content',
            new_name='tutorial_content',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='series',
            new_name='tutorial_series',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='slug',
            new_name='tutorial_slug',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='title',
            new_name='tutorial_title',
        ),
        migrations.RenameField(
            model_name='tutorialcategory',
            old_name='category',
            new_name='tutorial_category',
        ),
        migrations.RenameField(
            model_name='tutorialcategory',
            old_name='slug',
            new_name='tutorial_slug',
        ),
        migrations.RenameField(
            model_name='tutorialcategory',
            old_name='summary',
            new_name='tutorial_summary',
        ),
        migrations.RenameField(
            model_name='tutorialseries',
            old_name='category',
            new_name='tutorial_category',
        ),
        migrations.RenameField(
            model_name='tutorialseries',
            old_name='series',
            new_name='tutorial_series',
        ),
        migrations.RenameField(
            model_name='tutorialseries',
            old_name='summary',
            new_name='tutorial_summary',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='published',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 13, 35, 22, 894960), verbose_name='date published'),
        ),
    ]