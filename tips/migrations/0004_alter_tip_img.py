# Generated by Django 3.2.4 on 2021-07-13 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0003_alter_tip_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/tips', verbose_name='이미지'),
        ),
    ]
