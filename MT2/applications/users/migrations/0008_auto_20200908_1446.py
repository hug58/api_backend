# Generated by Django 3.1 on 2020-09-08 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_remove_friends_friend'),
        ('users', '0007_auto_20200908_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, to='friends.Friends'),
        ),
    ]