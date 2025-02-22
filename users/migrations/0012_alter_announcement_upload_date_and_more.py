# Generated by Django 5.0.4 on 2024-05-08 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_teacher_user_alter_topics_uploader_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 8, 9, 9, 44, 598093, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 8, 9, 9, 44, 598093, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_messaged',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 8, 9, 9, 44, 598093, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 8, 9, 9, 44, 598093, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forum',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 8, 9, 9, 44, 598093, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='topiccomments',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 8, 9, 9, 44, 598093, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='topics',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 8, 9, 9, 44, 598093, tzinfo=datetime.timezone.utc)),
        ),
    ]
