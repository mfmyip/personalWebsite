# Generated by Django 3.1 on 2023-03-15 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20230315_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='projects/static/img/'),
        ),
    ]
