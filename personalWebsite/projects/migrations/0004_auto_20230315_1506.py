# Generated by Django 3.1 on 2023-03-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20230315_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
