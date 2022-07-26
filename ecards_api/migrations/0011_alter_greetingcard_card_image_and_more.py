# Generated by Django 4.0.6 on 2022-08-02 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecards_api', '0010_alter_greetingcard_card_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greetingcard',
            name='card_image',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='greetingcard',
            name='card_image_file',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='card_images'),
        ),
    ]
