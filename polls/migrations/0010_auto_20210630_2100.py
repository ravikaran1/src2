# Generated by Django 3.1.5 on 2021-06-30 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20210630_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='question',
            field=models.TextField(),
        ),
    ]
