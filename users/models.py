from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.utils import timezone
# Create your models here.

now = timezone.now()


class Forum(models.Model):
    
    file = models.FileField(
        upload_to='media/announcement',
        validators=[ 
            FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'pdf', 'word', 'ppt', 'xlsx', 'csv', 'gif'])
        ],
        null=True,  # Allow null values
        blank=True  # Also allow empty values (in forms)
    )
    upload_date = models.DateTimeField(default=now)
    description = models.TextField()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Topics(models.Model):
    
    file = models.FileField(
        upload_to='media/topics',
        validators=[
            FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'pdf','mp3', 'mp4' 'word', 'ppt', 'xlsx', 'csv', 'gif'])
        ],
        null=True,  # Allow null values
        blank=True  # Also allow empty values (in forms)
    )
    upload_date = models.DateTimeField(default=now)
    description = models.TextField()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)


class Announcement(models.Model):
    
    file = models.FileField(
        upload_to='media/announcement',
        validators=[
            FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'pdf', 'word', 'ppt', 'xlsx', 'csv', 'gif'])
        ],
        null=True,  # Allow null values
        blank=True  # Also allow empty values (in forms)
    )
    upload_date = models.DateTimeField(default=now)
    description = models.TextField()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name='liked_announcements', blank=True)

class Comments(models.Model):
    post = models.ForeignKey(Forum, on_delete=models.CASCADE)
    commentors = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(default=now)


class TopicComments(models.Model):
    post = models.ForeignKey(Topics, on_delete=models.CASCADE)
    commentors = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(default=now)


class Events(models.Model):
    
    file = models.FileField(upload_to='media/event', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'pdf', 'word', 'ppt', 'xlsx', 'csv', 'gif'])],)
    upload_date = models.DateTimeField(default=now)
    description = models.TextField()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField()


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    message = models.TextField()
    date_messaged = models.DateTimeField(default=now)
    
    
    


class Webinar(models.Model):
    
    file = models.FileField(
        upload_to='media/webinar',
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4'])
        ],
        null=True,  # Allow null values
        blank=True  # Also allow empty values (in forms)
    )
    upload_date = models.DateTimeField(default=now)
    description = models.TextField()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)