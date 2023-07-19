from django.db import models
from painless.models.mixins import TimestampMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxLengthValidator
from ..helpers.text_choices import GenderOptions
from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth import get_user_model
User = get_user_model()

class Profile(TimestampMixin):
    
    gender = models.CharField(_("Gender"),max_length=10,choices=GenderOptions.choices,null=True,blank=True,help_text=_("User's Gender")) 
    user = models.OneToOneField(User,verbose_name=_("User"),related_name='profile',on_delete=models.CASCADE,help_text=_("the user's profile information"))
    
    class Meta :
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        
    def __str__(self):
        return self.user.phone_number
    
    def __repr__(self):
        return self.user.phone_number
    