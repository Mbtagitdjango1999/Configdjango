from decouple import config

from .base import *
from .services import *
from .packages import * 



#breakpoint()

DEBUG= config('DEBUG',cast=bool,default=True)