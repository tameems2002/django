# Generated by Django 3.0.4 on 2020-04-04 08:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200402_0235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='url',
        ),
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(max_length=250),
        ),
    ]
