# Generated by Django 3.2.5 on 2021-07-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20210721_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='profile_photo',
            field=models.FileField(blank=True, upload_to='account_files/profile_photos/'),
        ),
    ]
