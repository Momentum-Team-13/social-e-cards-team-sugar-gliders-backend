# Generated by Django 4.0.6 on 2022-07-27 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecards_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='follower',
            new_name='following',
        ),
    ]