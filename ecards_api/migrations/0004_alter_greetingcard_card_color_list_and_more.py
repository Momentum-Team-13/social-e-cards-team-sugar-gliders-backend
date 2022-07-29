# Generated by Django 4.0.6 on 2022-07-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecards_api', '0003_follow_user_alter_follow_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greetingcard',
            name='card_color_list',
            field=models.CharField(choices=[('00FF00', '00FF00'), ('ff0000', 'ff0000'), ('0000FF', '0000FF')], default='00FF00', max_length=7),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_following'),
        ),
    ]