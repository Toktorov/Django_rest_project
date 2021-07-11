# Generated by Django 2.2.6 on 2021-07-11 14:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_auto_20210710_0718'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Movie',
        ),
        migrations.RenameModel(
            old_name='PostImage',
            new_name='MovieImage',
        ),
        migrations.RenameField(
            model_name='movieimage',
            old_name='post',
            new_name='movie',
        ),
    ]
