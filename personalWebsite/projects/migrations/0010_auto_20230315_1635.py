# Generated by Django 3.1 on 2023-03-15 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20230315_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/projects/static/img/'),
        ),
    ]
