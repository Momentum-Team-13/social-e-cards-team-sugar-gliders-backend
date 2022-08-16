# Generated by Django 4.0.6 on 2022-08-02 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecards_api', '0014_alter_greetingcard_card_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greetingcard',
            name='card_color_list',
            field=models.CharField(choices=[('00FF00', '00FF00'), ('ff0000', 'ff0000'), ('0000FF', '0000FF')], default='00FF00', max_length=200),
        ),
        migrations.AlterField(
            model_name='greetingcard',
            name='card_image',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='greetingcard',
            name='card_image_file',
            field=models.ImageField(blank=True, max_length=600, null=True, upload_to='card_images'),
        ),
    ]
