from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models.mixins import TimestampMixin,BannerOperationMixin,PictureOperationMixin
# Create your models here.



class ServiceAttachment(TimestampMixin):
    
    class Meta:
        verbose_name = _("Service Attachment")
        verbose_name_plural = _("Service Attachments")
        
    
    title = models.CharField(verbose_name=_("Title"), max_length=100,unique=True,null=False,help_text='Service Name')
    attachment = models.FileField(_("Attachment"),upload_to='attachments/')
    service = models.ForeignKey('Service',on_delete=models.CASCADE,related_name="attachments",help_text=_("relation for many to one from service to attachment"))
    
    
    def __str__(self):
        return self.title
    
    def __repr__(self) :
        return self.title
    