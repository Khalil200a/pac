# Generated by Django 2.2.6 on 2021-08-10 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0012_auto_20210810_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Filter',
        ),
    ]
