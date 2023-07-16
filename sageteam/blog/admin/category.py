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
    
    #if you want use auto_complete_field in post you must have search field in category beacause the category_id is a foreignKEY in posts
    search_fields =(
        'title',
    )