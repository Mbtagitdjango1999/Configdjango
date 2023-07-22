from kernel.settings.base import DEFAULT_APPS

BUSINESS_APPS=[
   "account",
   'sageteam.service',
   'sageteam.blog',
   'painless'
]


LOCAL_APPS = [
   'rest_framework',
]

INSTALLED_APPS=DEFAULT_APPS+BUSINESS_APPS + LOCAL_APPS