# Generated by Django 4.0.6 on 2022-08-02 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecards_api', '0016_alter_greetingcard_card_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greetingcard',
            name='card_image_file',
        ),
    ]
