# Generated by Django 3.1 on 2020-09-18 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200918_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.TextField(null=True),
        ),
    ]
