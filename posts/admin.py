from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 
        'subtitle', 
        'created_at']

# Register your models here.

admin.site.register(Post, PostAdmin)