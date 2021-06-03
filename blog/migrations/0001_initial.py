# Generated by Django 3.1.4 on 2021-05-22 16:46

import autoslug.fields
import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('issue', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=20, populate_from='title')),
                ('desc', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('thumbnail', models.ImageField(blank='true', upload_to='', validators=[blog.models.post.validate_image])),
            ],
        ),
    ]
