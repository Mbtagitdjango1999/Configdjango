from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
    
    
    #this is for signals that django know them
    def ready(self) :
        import account.signals
