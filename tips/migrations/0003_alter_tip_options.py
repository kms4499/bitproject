# Generated by Django 3.2.4 on 2021-07-13 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0002_alter_tip_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tip',
            options={'verbose_name': '법률팁', 'verbose_name_plural': '법률팁'},
        ),
    ]