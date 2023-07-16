import secrets 
import os
from pathlib import Path
from django.conf import settings
from sageteam.blog.models import Category ,Tag ,Post

from painless.models.generator import BaseDataGenerator

#this package for tell to django we have fake data upload 
#by this package we can upload file without what validator in db and backend
from django.core.files.uploadedfile import SimpleUploadedFile
# from django.conf import settings
from tqdm import tqdm
#tqdm from create bulki data usage 
from kernel.settings.base import BASE_DIR
# settings.configured.

BASE_DIR11 = Path(__file__).resolve().parent.parent.parent.parent.parent


BASEDIR = BASE_DIR

class BlogDataGeneratorLayer(BaseDataGenerator):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)



    def create_post_categories(self,total):
        # for i in tqdm(range(total)):
        #     Category.objects.create(title = f"category{secrets.token_urlsafe(10)}")
            
        objs = [
            Category(
                title = f"Categorey_title--->{secrets.token_urlsafe(10)}",
                slug = f'Category_slug--->{self.get_random_secret()}',
                )
            for i in tqdm(range(total)) 
            
            
        ]
        
        categories =Category.objects.bulk_create(objs,batch_size=10_000)
        return categories
        
        
        
        
    def create_tags(self,total):
        objs = [
            Tag(
                title = f"Tags_title--->{secrets.token_urlsafe(10)}",
                slug = f'Tags_slug--->{self.get_random_secret()}',
                )
            for i in tqdm(range(total)) 
            
        ]    
        
        tags =Tag.objects.bulk_create(objs,batch_size=10_000)
        return tags
    
    
    def create_posts(self,categories,tags,total):
        # BaseDataGenerator.get_random_secret() = self.get_random_secret() forrrrr just OOP
        demo_pic_path = os.path.normpath(f"media/demo/3EroTL.jpg")
        with open(os.path.join(BASEDIR,demo_pic_path),mode='rb')as pic_file:
            
            pic= pic_file.read()
            
        objs = [                    
            Post(
                title = f"Post_title--->{self.get_random_secret()}",
                slug = f'Post_slug--->{self.get_random_secret()}',
                #summary = f"Post_summary--->{self.get_random_secret()}",
                summary = self.get_random_words(15),
                description = self.get_random_sentence(10),
                priority = i+1,
                category = self.get_random_objs(categories),
                picture = SimpleUploadedFile(name=self.get_random_pic_name(),content= pic),
                pic_alternate_text = self.get_random_words(6),
                )
            
            
            
            
            
            for i in tqdm(range(total)) 
            
        ]    
        
        posts =Post.objects.bulk_create(objs,batch_size=10_000)
        return posts
        