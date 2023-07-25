from rest_framework import serializers
from sageteam.blog.models import Category



class CategorySerilizer(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = ['title' , 'slug']