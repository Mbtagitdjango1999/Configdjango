from django.utils.deconstruct import deconstructible
from django.core.validators import BaseValidator
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

@deconstructible
class DimensionValidator(BaseValidator):
    code = 'dimension_value'
    
    def __init__(self,width , height ):
        self.width = width
        self.height =height
        
    def __call__(self, value):
        pic= value.file.open() 
        width , height = get_image_dimensions(pic)
        if not (width ==self.width and height == self.height):
            raise ValidationError(
                _(f"it most in {self.height} for height and {self.width} for width")
            )