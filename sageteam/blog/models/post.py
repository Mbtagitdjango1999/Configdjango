from django.db import models
from django.utils.translation import gettext_lazy as _
from painless.models.validator.picture import DimensionValidator
from painless.models.mixins import TitleSlugMixin,TimestampMixin,BannerOperationMixin,TitleSlugDescriptionMixin,PictureOperationMixin
from django.core.validators import FileExtensionValidator 
# from .tag import Tag

from ..repository.manager import PostDataAccessLayerManager

# class Tag(TitleSlugMixin,TimestampMixin) :
#     class Meta :
#         verbose_name = _("Tag")
#         verbose_name_plural = _("Tags") 
          
#     def __str__(self) -> str:
#         return self.title
#     def __repr__(self) -> str:
#         return self.title    
        



class Post(TimestampMixin,TitleSlugDescriptionMixin,PictureOperationMixin):
    summary = models.CharField(_("Summary"),max_length=255)
    priority = models.PositiveSmallIntegerField(_("Priority"), )
    picture = models.ImageField(_("Picture"),upload_to="blog/post",width_field="pic_width_field",height_field="pic_height_field",max_length=110,validators=[DimensionValidator(800 ,600),FileExtensionValidator(allowed_extensions=['JPG','JPEG','jpg','jpeg'])])
    category = models.ForeignKey("Category",verbose_name="Category",on_delete=models.PROTECT,related_name='posts',help_text=_("access to all post by category"),blank=True,null=True)
    tags = models.ManyToManyField("Tag",verbose_name="Tags",related_name='posts',help_text=_("access to all posts by tags"),blank=True)
    
    #this is part that we work by querysets
    dal = PostDataAccessLayerManager()
    #if we dont wite this part we cannt use post.objects beacause its not in us hand after declare "dal" or "bll"
    #so we declare objects in other part to use objects
    #because in futuer if we install package <>that package dont know manager(objects) so we declare it in other hand to reach manager(objects)  
    objects = models.Manager()
    
    
    def __str__(self) -> str:
        return self.title
    def __repr__(self) -> str:
        return self.title
    
    
    class Meta :
        verbose_name = _("Post")
        verbose_name_plural = _("Posts") 
    
   
    
    
# class PostCategory(TitleSlugMixin,TimestampMixin) :
#     class Meta :
#         verbose_name = _("Post Category")
#         verbose_name_plural = _("Post Categories") 
          
#     def __str__(self) -> str:
#         return self.title
#     def __repr__(self) -> str:
#         return self.title
    
    
# class PostTag(TitleSlugMixin,TimestampMixin) :
#     class Meta :
#         verbose_name = _("Post Tag")
#         verbose_name_plural = _("Posts Tags") 
          
#     def __str__(self) -> str:
#         return self.title
#     def __repr__(self) -> str:
#         return self.title    
    
    
