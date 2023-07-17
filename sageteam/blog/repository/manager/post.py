from django.db.models import Manager

from ..queryset.post import PostDataAccessQuerySet

class PostDataAccessLayerManager(Manager):
    def get_queryset(self):
        return PostDataAccessQuerySet(self.model,using=self._db)
    
    
    def find_by_category(self,category_slug:str):
    # self ---->>>> self=post__---__>>post.objects = self.objects
        return self.get_queryset().find_by_category(category_slug=category_slug)
   
   
    def get_total_posts(self):
    # self ---->>>> self=post__---__>>post.objects = self.objects
        return self.get_queryset().get_total_posts()
    
    
    def get_total_posts_by_related_category(self):
    # self ---->>>> self=post__---__>>post.objects = self.objects
        return self.get_queryset().get_total_posts_by_related_category()
    
    
    def get_total_posts_by_related_tags(self):
    # self ---->>>> self=post__---__>>post.objects = self.objects
        return self.get_queryset().get_total_posts_related_by_tags()
    
    