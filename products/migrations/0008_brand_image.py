# Generated by Django 3.2 on 2022-07-30 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20220725_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(default=' ', upload_to='brand/', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
