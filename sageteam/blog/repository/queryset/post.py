from django.db.models import QuerySet


class PostDataAccessQuerySet(QuerySet):
    def find_by_category(self,category_slug:str):
        # self ---->>>> self=post__---__>>post.objects = self.objects
        #return self.filter(category__slug = category_slug)
        return self.get_total_posts_by_related_category()\
            .filter(category__slug = category_slug)
    
    #fuuuuuucckkkkk \\\\ 
    def get_total_posts(self):
        return self.get_total_posts_by_related_category()\
        .get_total_posts_related_by_tags()
    
    
    def get_total_posts_by_related_category(self):
        return self.select_related('category')
    
    def get_total_posts_related_by_tags(self):
        return self.prefetch_related('tags')