# Generated by Django 2.2.6 on 2021-08-09 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_auto_20210809_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='users/pdfs'),
        ),
        migrations.AddField(
            model_name='produit',
            name='pdf2',
            field=models.FileField(blank=True, null=True, upload_to='users/pdfs'),
        ),
    ]
