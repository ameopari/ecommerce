# Generated by Django 3.2.6 on 2022-02-23 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=80)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='product_images')),
            ],
        ),
    ]
