from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    #field
    class Meta:
        model = Post
        fields = ['id','title','url','poster','created']
    
    