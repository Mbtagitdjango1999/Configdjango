from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models.mixins import TitleSlugMixin,TimestampMixin,BannerOperationMixin,TitleSlugDescriptionMixin,PictureOperationMixin
  
    
class Category(TitleSlugMixin,TimestampMixin) :
    class Meta :
        verbose_name = _("Category")
        verbose_name_plural = _("Categories") 
          
    def __str__(self) -> str:
        return self.title
    def __repr__(self) -> str:
        return self.title
    