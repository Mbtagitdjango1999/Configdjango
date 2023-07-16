from django.contrib import admin
#from ..models.service import Service 
from sageteam.service.models import Service,ServiceAttachment
from django.utils.translation import gettext_lazy as _

# Register your models here.

#this field for many to one relatrion from oneeeee to manyyyyyyy
class AttachmentInlineAdmin(admin.StackedInline):
    model = ServiceAttachment
    #this is for count of attachment for any service
    min_num = 1
    extra = 4
    max_num = 3
    verbose_name = _("Attttaachhmennnnt")
    verbose_name_pulral = _("Attttaachhmennnnts")
    can_delete = False
    show_change_link = True 

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'summary',
        'created',
        'modified',
                    )
    
    search_fields = (
        'title',
        'summary',
        'description',
    )
    
    search_help_text =_("Search by kon taghar and  title,summary,description")
    
    list_filter = (
        'created',
        'modified',
    )
    
    save_on_top =True
    
    #this field for Inlineeeee relations
    inlines = (
        AttachmentInlineAdmin,
        
    )
    
    
    
    
    
    fieldsets = (
        
        (_("Service Information"),{'classes':('collapse',),"fields":('title',
        'summary',
        'description')}),
        
           (_("Picture Management"),{'classes':('collapse',),"fields":('icon',
            'picture',
            'pic_alternate_text',
            'banner',
            'banner_alternate_text',
            'pic_width_field',
            'pic_height_field',
            'banner_width_field',
            'banner_height_field'
            
            
        )}),
        
        (_("Security Center"),{'classes':('collapse',),"fields":( 'created',
        'modified')}),
        
    )
    
    readonly_fields = (
           'created',
           'modified',
           'pic_width_field',
           'pic_height_field',
           'banner_width_field',
           'banner_height_field'
         
            )
    
    