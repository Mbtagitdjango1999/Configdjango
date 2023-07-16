from django.core.management.base import BaseCommand, CommandParser

from sageteam.blog.repository.generator import BlogDGL


class Command(BaseCommand): 
    
    
    def add_arguments(self,parser):
        
        parser.add_argument('--cat-total', type = int,default=10)
        parser.add_argument('--tag-total', type = int,default=10)
    
    
    
    def handle(self,*args, **kwargs):
        #this means when dont tell it in Command that what range total you create by default 10_000
        cat_total = int(kwargs.get('--cat-total',10_000))
        tag_total = int(kwargs.get('--tag-total',10_000))
        DGL = BlogDGL()
        categories = DGL.create_post_categories(cat_total)
        tags = DGL.create_tags(total=tag_total)
        posts = DGL.create_posts(categories=categories,tags=tags,total=2000)