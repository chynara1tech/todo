# Generated by Django 3.1.3 on 2021-01-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210120_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='is_favorites',
            field=models.BooleanField(default=False),
        ),
    ]