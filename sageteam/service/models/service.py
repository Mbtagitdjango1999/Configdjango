from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models.mixins import TimestampMixin,PictureOperationMixin,BannerOperationMixin,TitleSlugDescriptionMixin
# Create your models here.


class Service(TitleSlugDescriptionMixin,TimestampMixin,PictureOperationMixin,BannerOperationMixin):

    #title = models.CharField(verbose_name=_("Title"), max_length=100,unique=True,null=False,help_text='Service Name')
    summary = models.CharField(_("Summary"),max_length=200,unique=True,null=True,help_text='Service summary')
    #description = models.TextField(_("Description"),help_text='Description of Service')
    icon = models.CharField(_("Icon"),max_length=50,unique=True,help_text=_("Icon of service"))
    
    picture = models.ImageField(_("Picture"),max_length=110,height_field='pic_height_field',width_field='pic_width_field',upload_to = 'service/')
    
    
    # pic_height_field = models.PositiveSmallIntegerField(
    #     null=True,blank=True,editable=False,help_text="Size of Picture's height"
    # )
    
    # pic_width_field = models.PositiveSmallIntegerField(
    #     null=True,blank=True,editable=False,help_text="Size of Picture's width"
    # )
    
    # pic_alternate_text = models.CharField(
    #     max_length=110,
    #     help_text= 'Description about picture that is uploaded.'
    # )
    
    
    banner = models.ImageField(_("Banner"),max_length=110,height_field='banner_height_field',width_field='banner_width_field',upload_to = 'banner/')
    
    
    # banner_height_field = models.PositiveSmallIntegerField(
    #     null=True,blank=True,editable=False,help_text="Size of Picture's height"
    # )
    
    # banner_width_field = models.PositiveSmallIntegerField(
    #     null=True,blank=True,editable=False,help_text="Size of Picture's width"
    # )
    
    # banner_alternate_text = models.CharField(
    #     max_length=110,
    #     help_text= 'Description about banner that is uploaded.'
    # )  
    
    
    # created = models.DateTimeField(_("Created"),auto_now_add=True,help_text='auto insertion')
    # modified = models.DateTimeField(_("Modified"),auto_now=True,help_text='auto mification')
    
    def __str__(self):
        return self.title
    
    def __repr__(self) :
        return self.title