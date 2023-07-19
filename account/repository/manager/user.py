from django.contrib.auth.base_user import BaseUserManager
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _

from ..queryset import UserQuerySet

class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def get_queryset(self):
        return UserQuerySet(self.model , using=self._db)
    
    def _create_user(self,phone_number,password,**extra_fields):
        if not phone_number :
            raise ValueError('`phone_number` must be set.')
        
        user = self.model(phone_number = phone_number,**extra_fields) 
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_user(self,phone_number , password = None , **extra_fields) :
        extra_fields.setdefault('is_superuser' , False)
        extra_fields.setdefault('is_active',False)
        return self._create_user(phone_number=phone_number,password=password,**extra_fields)
    
    
    def create_active_user(self,phone_number , password = None , **extra_fields) :
        extra_fields.setdefault('is_superuser' , False)
        extra_fields.setdefault('is_active',True)
        return self._create_user(phone_number=phone_number,password=password,**extra_fields)
    
    
    def create_staff_user(self,phone_number , password = None , **extra_fields) :
        extra_fields.setdefault('is_superuser' , False)
        extra_fields.setdefault('is_staff',True)
        return self._create_user(phone_number=phone_number,password=password,**extra_fields)
    
    
    def create_superuser(self , phone_number , password= None,**extra_fields):
        extra_fields.setdefault('is_superuser' , True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_staff',True)
        
        if extra_fields.get('is_staff') is not True :
            raise ValueError(_('Superuser must have `is_staff = True`'))
        
        if extra_fields.get('is_superuser') is not True :
            raise ValueError(_('Superuser must have `is_superuser = True`'))
        
        if extra_fields.get('is_active') is not True :
            raise ValueError(_('Superuser must have `is_active = True`'))
        
        return self._create_user(phone_number,password,**extra_fields)
    
    
    
class UserDataAccessLayer(UserManager):
    def get_actives(self , is_active = True):
        return self.get_queryset().get_actives(is_active)
    