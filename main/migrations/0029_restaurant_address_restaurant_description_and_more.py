# Generated by Django 4.1.6 on 2023-03-04 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_alter_product_image3d'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='video_url',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('Text', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='media/uploads/awards', verbose_name='Product Photo')),
                ('Restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.restaurant')),
            ],
        ),
    ]
