# Generated by Django 4.1.4 on 2022-12-21 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='ended_on',
        ),
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to='rareapi.user'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='created_on',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='follower_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='rareapi.user'),
        ),
    ]
