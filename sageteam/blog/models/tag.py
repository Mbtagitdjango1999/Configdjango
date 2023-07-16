from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models.mixins import TitleSlugMixin,TimestampMixin,BannerOperationMixin,TitleSlugDescriptionMixin,PictureOperationMixin
 

class Tag(TitleSlugMixin,TimestampMixin) :
    class Meta :
        verbose_name = _("Post Tag")
        verbose_name_plural = _("Posts Tags") 
          
    def __str__(self) -> str:
        return self.title
    def __repr__(self) -> str:
        return self.title    
    