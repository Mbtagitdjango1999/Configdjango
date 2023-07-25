# from .....kernel.settings.base import MEDIA_ROOT,MEDIA_URL
# from django.conf.urls.static import static

# MEDIA_URL = '/media/'


from django.core.management.base import BaseCommand, CommandParser

from account.repository.generator.user import UserDataGenerator 


class Command(BaseCommand): 
    
    
    def add_arguments(self,parser):
        
        parser.add_argument('--cat-total', type = int,default=10)
        parser.add_argument('--tag-total', type = int,default=10)
    
    
    
    def handle(self,*args, **kwargs):
        #this means when dont tell it in Command that what range total you create by default 10_000
        cat_total = int(kwargs.get('--cat-total',10))
        tag_total = int(kwargs.get('--tag-total',10))
        DGL = UserDataGenerator()
        users = DGL.create_user(10)
        # categories = DGL.create_post_categories(cat_total)
        # tags = DGL.create_tags(total=tag_total)
        # posts = DGL.create_posts(categories=categories,total=20)
        # posts = DGL.join_tags_to_posts(posts=posts,tags=tags,item_per_obj=3)
        #print(static(MEDIA_URL,document_root = MEDIA_ROOT))
        