from django.contrib import admin
#from ..models.attachment import ServiceAttachment
#from service.models import ServiceAttachment
from django.utils.translation import gettext_lazy as _
from sageteam.service.models import ServiceAttachment
# Register your models here.

@admin.register(ServiceAttachment)
class ServiceAttachmentAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created',
        'modified',
                    )
    
    
    
    list_filter = (
        
        'created',
        'modified',
    )
