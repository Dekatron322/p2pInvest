# Generated by Django 3.1.7 on 2021-07-20 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appuser',
            old_name='first_name',
            new_name='full_name',
        ),
    ]