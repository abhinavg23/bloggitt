# Generated by Django 3.1.4 on 2021-05-29 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210529_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
