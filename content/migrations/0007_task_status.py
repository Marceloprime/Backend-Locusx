# Generated by Django 2.2.13 on 2021-05-06 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20210505_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
