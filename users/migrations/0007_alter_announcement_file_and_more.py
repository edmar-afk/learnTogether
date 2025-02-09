# Generated by Django 5.0.4 on 2024-04-27 23:41

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_announcement_upload_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/announcement', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'pdf', 'word', 'ppt', 'xlsx', 'csv', 'gif'])]),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 23, 41, 52, 716298, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 23, 41, 52, 716298, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='file',
            field=models.FileField(upload_to='media/event', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'pdf', 'word', 'ppt', 'xlsx', 'csv', 'gif'])]),
        ),
        migrations.AlterField(
            model_name='events',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 23, 41, 52, 716298, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forum',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/announcement', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'pdf', 'word', 'ppt', 'xlsx', 'csv', 'gif'])]),
        ),
        migrations.AlterField(
            model_name='forum',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 23, 41, 52, 716298, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='topiccomments',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 23, 41, 52, 716298, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='topics',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/topics', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'pdf', 'word', 'ppt', 'xlsx', 'csv', 'gif'])]),
        ),
        migrations.AlterField(
            model_name='topics',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 23, 41, 52, 716298, tzinfo=datetime.timezone.utc)),
        ),
    ]
