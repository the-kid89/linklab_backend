# Generated by Django 2.1 on 2018-08-12 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_userprofile_discord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialdisplaysettings',
            name='position',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]