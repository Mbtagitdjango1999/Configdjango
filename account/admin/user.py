from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from account.models import Profile

User = get_user_model()


class PRofileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = "Profile"
    verbose_name_plural = "Profiles"
    fk_name = "user"
    radio_fields ={
        "gender" : admin.VERTICAL
        
    }


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'phone_number',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login',
        'date_joined',
    )
    
    
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login',
        'date_joined',
        
    )
    
    
    search_fields = (
        'phone_number',
        'email',
        'first_name',
        'last_name',
        
    )
    
    inlines = (
        PRofileInline,
    )
    
    
    search_help_text = "you can find users by phone_number,email,first_name,last_name"
    
    
    
    