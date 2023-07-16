import secrets
import random
from mimesis import Locale
 
from mimesis import (
    
    Text,
    Person,
    Numeric,
    Finance,
    Datetime,
    Address,
    Food 
)

#generate random String
class BaseDataGenerator:
    
    def __init__(self,locale ='en') :
        
        self.person = Person(getattr(Locale,locale.upper()))
        self.text = Text(getattr(Locale,locale.upper()))
        self.finance = Finance(getattr(Locale,locale.upper()))
        
        
    def get_random_secret(self , nbytes = 20):
        return secrets.token_urlsafe(nbytes)
    
    def get_random_sentence(self , total):
        return self.text.text(quantity=total)
    
    def get_random_words(self , total):
        words = self.text.words(quantity=total)
        
        return ' '.join(words)
    
    def get_random_objs(self , population):
        return random.choice(population)
    
    def get_random_pic_name(self , format = 'jpg',prefix= 'generated__pic--'):
        return f'{prefix}-{self.get_random_secret(6)}.{format}'