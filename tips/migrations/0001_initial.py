# Generated by Django 3.2.4 on 2021-07-13 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지')),
                ('video_key', models.CharField(max_length=15, verbose_name='비디오키')),
                ('created_date', models.DateTimeField(blank=True, null=True, verbose_name='작성일')),
            ],
            options={
                'verbose_name': '법률팁',
                'verbose_name_plural': '법률팁',
                'db_table': '법률팁',
            },
        ),
    ]
