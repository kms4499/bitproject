# Generated by Django 3.2.4 on 2021-07-12 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0005_auto_20210712_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='댓글작성일시'),
        ),
        migrations.AlterField(
            model_name='free',
            name='create_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='등록시간'),
        ),
    ]
