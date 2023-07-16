from typing import Any
from django.db import models
from django.utils.translation import gettext_lazy as _

__all__=[
    'TitleSlugMixin','TitleSlugDescriptionMixin'
]

x=10

class TitleSlugMixin(models.Model):
    
    #az amd  help_text vase title nazashtim ta toye  har classi ke raft az init esm on class ro begire bezare help_text
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.__class__.title.field.help_text =_(
            "Title of {0}".format(self.__class__.__name__)
        )
   
    title = models.CharField(_("Title"),max_length=100,unique=True)
    slug = models.SlugField(_("Slug"),max_length=110,editable=False,allow_unicode = True,help_text=_("sluggggg"))
    
    class Meta:
        
        abstract = True
         
         
         
class TitleSlugDescriptionMixin(TitleSlugMixin):
    
    description = models.TextField(_("Description"),help_text=_("Long description"),)
    
    class Meta:
        
        abstract = True
                  