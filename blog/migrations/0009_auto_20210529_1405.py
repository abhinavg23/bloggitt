# Generated by Django 3.1.4 on 2021-05-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210529_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
