# Generated by Django 4.1.3 on 2023-02-05 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_text3d'),
    ]

    operations = [
        migrations.AddField(
            model_name='text3d',
            name='hide',
            field=models.BooleanField(default=True),
        ),
    ]
