from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at') # Fields to display in the admin list view
    list_filter = ('created_at', 'updated_at') # Filters for the admin list view
    search_fields = ('title', 'content') # Searchable fields in the admin list view
    readonly_fields = ('created_at', 'updated_at') # Fields that are read-only in the admin detail view
    prepopulated_fields = {"title": ("title",)} # Prepopulate the title field in the admin detail view