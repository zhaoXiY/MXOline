# Generated by Django 2.2 on 2020-05-06 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200506_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('female', '女'), ('male', '男')], max_length=6, verbose_name='性别'),
        ),
    ]
