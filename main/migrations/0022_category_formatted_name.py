# Generated by Django 4.1.3 on 2023-02-05 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='formatted_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
