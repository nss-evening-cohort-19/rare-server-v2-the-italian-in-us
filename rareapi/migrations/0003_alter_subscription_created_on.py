# Generated by Django 4.1.4 on 2022-12-14 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0002_alter_user_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
