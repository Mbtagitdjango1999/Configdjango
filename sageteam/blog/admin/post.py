from django.contrib import admin

from sageteam.blog.models import Post
from django.utils.translation import gettext_lazy as _


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        #'title',
        'view_title',
        'slug',
        'priority',
        'category', 
        'created',
        'modified',       
    )
    
    filter_horizontal = (
        'tags',
    )
    
    autocomplete_fields = (
        'category',
    )
        
    readonly_fields = (
           'created',
           'modified',
           'slug'
         
            )
    
    # fieldsets = (
    #     (_("Service Information"),{'classes':('collapse',),"fields":('title',
    #     'slug',
    #     'description')}),
    # )
    
    
    
    #its better to declare in model juuuuussssttttt this place 
    
    # so its cut to painless/model/mixins/TitleSlug
    
    # @admin.display(empty_value= _("--Empty--"))
    # def view_title(self,obj):
    #     return obj.title if len(obj.title)< 30 else (obj.title[:30]+ '...')