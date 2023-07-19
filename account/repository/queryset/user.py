from django.db.models import QuerySet

class UserQuerySet(QuerySet):
    
    def get_actives(self,is_active = True):
        qs = self.filter(is_active = True)
        return qs