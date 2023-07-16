from django.contrib import admin

from sageteam.blog.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug', 
        'created',
        'modified',       
    )