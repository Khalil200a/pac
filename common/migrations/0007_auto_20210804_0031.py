# Generated by Django 2.2.6 on 2021-08-04 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20210804_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='titre_other',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]