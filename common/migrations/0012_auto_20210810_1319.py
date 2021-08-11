# Generated by Django 2.2.6 on 2021-08-10 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_auto_20210809_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='filter',
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter', models.CharField(max_length=200)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Produit')),
            ],
        ),
    ]
