from django.db import models
from django.utils.translation import gettext_lazy as _


class GenderOptions(models.TextChoices):
    # these tuples has two objects that first object save in our data base and second show to user in frontend
    Male = ('male',_("Male"))
    Female = ('female',_('Female'))
    DoNotPreferToSay = ('prefer_not',_("Do Not Prefer To Say"))
    NonBinary = ('non_binary', _("Non Binary"))