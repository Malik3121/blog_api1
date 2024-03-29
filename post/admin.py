from django.contrib import admin
from .models import *
from review.models import Comment

# admin.site.register(Post)

# class PostAdmin(admin.ModelAdmin):
#     list_display=['title', 'category']
#     list_filter=['author', 'created_at']
#     search_fields=['body', 'title']

# admin.site.register(Post, PostAdmin)

class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Category)

