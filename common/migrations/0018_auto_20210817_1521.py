# Generated by Django 2.2.6 on 2021-08-17 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0017_formation_necessity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='necessity',
            field=models.IntegerField(blank=True),
        ),
    ]
