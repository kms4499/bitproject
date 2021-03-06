# Generated by Django 3.2.4 on 2021-07-12 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0004_alter_comment_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='free',
            name='hits',
            field=models.PositiveIntegerField(default=0, verbose_name='조회수'),
        ),
        migrations.AddField(
            model_name='free',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='글수정일시'),
        ),
    ]
