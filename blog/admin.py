from django.contrib import admin

# Register your models here.
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_public', 'created_date']
    list_display_links = ['title']
    list_editable = ['is_public']