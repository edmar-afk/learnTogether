from django.contrib import admin
from .models import Forum, Comments

class ForumAdmin(admin.ModelAdmin):
    list_display = ['id', 'upload_date', 'description', 'uploader']

admin.site.register(Forum, ForumAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'commentors', 'comment', 'comment_date']

admin.site.register(Comments, CommentsAdmin)
