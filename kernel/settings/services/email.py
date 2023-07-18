from decouple import config

if config('EMAIL_DEBUG', cast = bool):
    EMAIL_BACKEND = "django.core.mail.backend.console.EmailBackend"
    
    
    #when email_debug = True we have email and procec fake in our terminal
#TODO dsfsdf 
else :
    EMAIL_HOST = config('EMAIL_HOST' )
    EMAIL_PORT = config('EMAIL_PORT',cast = int)
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_USER_TLS = config('EMAIL_USER_TLS',default = True,cast=bool)
    DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
    ADMINS = config('ADMINS',
                    cast = lambda emails:[
                        email.strip() for email in emials.split(',')
                        ]
                    
                    )
        