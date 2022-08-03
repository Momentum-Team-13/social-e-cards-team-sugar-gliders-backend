# Generated by Django 4.0.6 on 2022-08-02 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecards_api', '0015_alter_greetingcard_card_color_list_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greetingcard',
            name='card_color',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='greetingcard',
            name='card_color_list',
            field=models.TextField(choices=[('00FF00', '00FF00'), ('ff0000', 'ff0000'), ('0000FF', '0000FF')], default='00FF00', max_length=200),
        ),
        migrations.AlterField(
            model_name='greetingcard',
            name='card_inner_message',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='greetingcard',
            name='card_outer_message',
            field=models.TextField(max_length=400),
        ),
    ]