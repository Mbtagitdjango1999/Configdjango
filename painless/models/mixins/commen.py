from typing import Any, Iterable, Optional
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.utils.text import slugify

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
    slug = models.SlugField(_("Slug"),max_length=110,editable=False,allow_unicode = True,help_text=_("sluggggg"),unique=True)
    
    class Meta:
        
        abstract = True
    
    #when you use this format instead of title you dont have any ordering so must be declare ordring in this part and you can change it's name from view_title to what ever you want in description
    @admin.display(empty_value= _("--Empty--"),ordering=('-title'),description=_("title"))
    def view_title(self):
        return self.title if len(self.title)< 30 else (self.title[:30]+ '...')    
         
    #this is for save automotly slug from title
    #in this method you musat be declare the super() 
    #allow_unicode help us to save persian in slug
    def save(self,*args, **kwargs) :
        self.slug = slugify(self.title , allow_unicode=True)
        super().save(*args, **kwargs)
        
         
class TitleSlugDescriptionMixin(TitleSlugMixin):
    
    description = models.TextField(_("Description"),help_text=_("Long description"),)
    
    class Meta:
        
        abstract = True
                  