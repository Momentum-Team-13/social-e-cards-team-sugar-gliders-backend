# Generated by Django 4.0.6 on 2022-08-01 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecards_api', '0005_alter_greetingcard_card_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='greetingcard',
            old_name='card_image',
            new_name='image',
        ),
    ]