# Generated by Django 3.1.7 on 2021-07-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20210727_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='due_date',
            field=models.CharField(default='none', max_length=500),
        ),
    ]
