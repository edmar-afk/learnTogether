# custom_filters.py

from django import template

register = template.Library()

@register.filter(name='is_image_extension')
def is_image_extension(file_name):
    allowed_extensions = ['png', 'jpeg', 'jpg', 'gif']
    extension = file_name.split('.')[-1].lower()
    return extension in allowed_extensions
