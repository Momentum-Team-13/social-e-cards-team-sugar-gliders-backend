# Generated by Django 4.0.6 on 2022-08-02 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecards_api', '0011_alter_greetingcard_card_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greetingcard',
            name='card_color',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='greetingcard',
            name='card_image_file',
            field=models.ImageField(blank=True, max_length=355, null=True, upload_to='card_images'),
        ),
    ]
