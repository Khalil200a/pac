# Generated by Django 2.2.6 on 2021-08-12 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0015_auto_20210810_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestation',
            name='necessity',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='produit',
            name='filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.Filters'),
        ),
    ]
