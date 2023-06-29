# Generated by Django 4.1.3 on 2023-02-06 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_text3d_hide'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='media/uploads/', verbose_name='Product Photo 3'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3d',
            field=models.FileField(default='default', upload_to='media/3dimages/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='media/uploads/', verbose_name='Product Photo 4'),
        ),
        migrations.AddField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='media/uploads/', verbose_name='Product Photo 5'),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='video',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='media/uploads/', verbose_name='Product Photo 2'),
        ),
    ]
