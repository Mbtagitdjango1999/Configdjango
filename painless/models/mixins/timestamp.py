from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampMixin(models.Model):
    class Meta :
        abstract = True
        
    
    created = models.DateTimeField(_("Created"),auto_now_add=True,help_text='auto insertion')
    modified = models.DateTimeField(_("Modified"),auto_now=True,help_text='auto mification')
        

   