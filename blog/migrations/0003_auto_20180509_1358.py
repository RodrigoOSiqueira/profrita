# Generated by Django 2.0.1 on 2018-05-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180504_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.AddField(
            model_name='post',
            name='capa',
            field=models.ImageField(blank=True, null=True, upload_to='blog/imagens', verbose_name='Capa'),
        ),
    ]
