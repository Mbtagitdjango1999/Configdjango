from typing import Any
from django.contrib.auth.models import AbstractUser
from painless.models.mixins import TimestampMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxLengthValidator,MinLengthValidator,RegexValidator,EmailValidator
from account.helpers.enums import RegexPatternEnum
from django.contrib.auth.validators import UnicodeUsernameValidator
import secrets

class User(AbstractUser,TimestampMixin):
    
    class Meta :
        verbose_name = _("User")
        verbose_name_plural = _("Users")
    
    #$create your custom User
    username_validator = UnicodeUsernameValidator()
    
    
    secret = models.CharField(max_length=43,unique=True,default=secrets.token_urlsafe,editable=False,help_text=_("user secret key use for encryption and token generation"))
    
    
    #username_validator = [RegexValidator(RegexPatternEnum.USERNAME),MaxLengthValidator(15),MinLengthValidator(3)]
    
    username = models.CharField(
        _("username"),
        max_length=15,
        unique=True,
        help_text=_(
            "Required. 15 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator,[RegexValidator(RegexPatternEnum.USERNAME),MaxLengthValidator(15),MinLengthValidator(3)],],
        error_messages={
            "unique": _("A user with that username already exists."),
            #this("min_length") is the code in validators you can read it in documention of MinLengthValidator
            #if you dont write any things it refrenced self of error message of these validtors
            "min_length":_("your user name must be more than 3 character")
        },
    )
    
    first_name = models.CharField(_('first name'),max_length=150,blank=True,null=True,validators=[RegexValidator(RegexPatternEnum.NAME),MaxLengthValidator(15),MinLengthValidator(3)])
    last_name = models.CharField(_("last name"),blank=True,null=True,validators=[RegexValidator(RegexPatternEnum.NAME),MaxLengthValidator(15),MinLengthValidator(3)])
    
    username = None
    phone_number = models.CharField(_("Phone Number"),max_length=15,unique=True,validators=[RegexValidator(RegexPatternEnum.IRAN_PHONE_NUMBER,MaxLengthValidator(15),MinLengthValidator(10)),],help_text=_('users'))
    email = models.EmailField(_('Email Adress'),blank=True,null=True,validators=[EmailValidator("email is valid")])
    
    
    USERNAME_FIELD = phone_number
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']
    
    
    #this a part you can dor bezanin vogode UserName ro and it refrenced phone_number instead of user_name
    @property
    def username(self):
        return self.phone_number
    
    def __str__(self):
        return f'{self.phone_number}'
    
    def __repr__(self):
        return f'{self.phone_number}'
    
    def email_user(self, subject: str, message: str, from_email: str = ..., **kwargs: Any) :
        return super().email_user(subject, message, from_email, **kwargs) 
    
    def send_message(self,subject,message):
        #send an sms to the instance user
        raise NotImplementedError 
    
    def send_otp(self,subject,message):
        #send an sms to the instance user
        raise NotImplementedError 
    #TODO write email service    
    