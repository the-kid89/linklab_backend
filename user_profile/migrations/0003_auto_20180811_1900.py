# Generated by Django 2.1 on 2018-08-11 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20180811_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialdisplaysettings',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service', to='user_profile.UserProfile'),
        ),
    ]