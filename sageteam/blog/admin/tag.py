from django.contrib import admin

from sageteam.blog.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug', 
        'created',
        'modified',       
    )