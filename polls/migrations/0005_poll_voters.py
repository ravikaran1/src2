# Generated by Django 3.1.5 on 2021-06-26 13:06

from django.db import migrations
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='voters',
            field=polls.models.ListField(default=[]),
        ),
    ]
