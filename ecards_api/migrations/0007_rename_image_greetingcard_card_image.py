# Generated by Django 4.0.6 on 2022-08-01 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecards_api', '0006_rename_card_image_greetingcard_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='greetingcard',
            old_name='image',
            new_name='card_image',
        ),
    ]
