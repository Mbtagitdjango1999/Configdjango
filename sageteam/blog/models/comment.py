from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user
from django.contrib.auth import get_user_model
from django.conf import settings
from painless.models.mixins import TitleSlugMixin,TimestampMixin,BannerOperationMixin,TitleSlugDescriptionMixin,PictureOperationMixin
from django.contrib.auth import get_user_model
User = get_user_model()
    #TODO asdasdas
class Comment(TimestampMixin) :
    class Meta :
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments") 
        
    text = models.TextField(_("Text"),max_length=500,help_text=_("Text content of the comment"))
    post = models.ForeignKey("Post" , on_delete=models.CASCADE,related_name='comments',help_text=_("Access to all comments from a post"))
    reply = models.ForeignKey("self",verbose_name=_("Reply"),on_delete=models.CASCADE,related_name="replies",help_text=_("Access to all reply frpm a comment"),blank=True,null=True)
    user = models.ForeignKey(User,verbose_name=_("User"),related_name="comments",on_delete=models.SET_NULL,help_text=_("the user reach all comments"),null=True)    
          
    def __str__(self) -> str:
        return self.title
    def __repr__(self) -> str:
        return self.title
    