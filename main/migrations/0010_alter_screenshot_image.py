# Generated by Django 4.1.1 on 2022-10-01 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_screenshots_screenshot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshot',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
