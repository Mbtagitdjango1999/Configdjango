import secrets
import logging
import random
from mimesis import Locale
from typing import List , Any
 
from mimesis import (
    
    Text,
    Person,
    Numeric,
    Finance,
    Datetime,
    Address,
    Food 
)

coreLogger =logging.getLogger('core')

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
    
    def add_to_m2m(self , objs:List[Any],target_field:str,item_per_obj:int,item):
        #add a number od random selected objects from a list to many to many fields
        #the method select `item_per_obj` number of objects randomly from the `objs`
        #List must not be empty , or an IndexError  will raised
        
        # objs : A list of objects to selec from .
        # target_field : the name of the ManyToManyField on the model instance
        # item_per_obj : the number of objects to add to the ManyToManyField .
        #item : the type of the model that the ManyToManyField belngs to. 
        
        
        #by getattr() ---> you can use:(className,attr)--->it give attr from that class to you.
        attr = getattr(item,target_field)
        try : 
            
            # (map(lambda _ :random.choice(objs),range(item_per_obj))
            items_to_add = list(map(lambda _ :random.choice(objs),range(item_per_obj)))    
            # items_to_add = 
            
            
            
            # for i in range(item_per_obj): 
            #     items_to_add = list(map(lambda yyyy :random.choice(yyyy),objs))
                
                    
           
         
        except IndexError as e:
            coreLogger.debug(
                "`objs` are empty. Please insert a Population data  ",
                exc_info=True
                )
            raise IndexError("`objs` are empty. Please insert a Population data  ")
        
        
        attr.add(*items_to_add)