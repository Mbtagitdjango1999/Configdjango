import os
from decouple import config

from kernel.settings.base import BASE_DIR

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LOCALE__PATHES = (
    os.path.join(BASE_DIR,config('TRANSLATION_DIR'))
)

