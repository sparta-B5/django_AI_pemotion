# Generated by Django 4.1.2 on 2023-02-10 05:55

import diary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, null=True, upload_to=diary.models.upload_to_func)),
                ('emotion_predict', models.TextField(null=True)),
                ('emotion_label', models.CharField(max_length=20, null=True)),
                ('emotion_percent', models.FloatField(null=True)),
                ('content', models.TextField(max_length=2200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '게시글',
                'verbose_name_plural': '게시글들',
                'db_table': 'diary',
            },
        ),
    ]
