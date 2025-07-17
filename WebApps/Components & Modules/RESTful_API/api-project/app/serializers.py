from rest_framework import serializers
from .models import Post, Vote

# serializer for post- select fileds from model for api
class PostSerializer(serializers.ModelSerializer):
    #make "poster" and "poster_id" fields read only
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')
    #add the field without models change
    votes = serializers.SerializerMethodField()
    #fields
    class Meta:
        #specify model from models.py
        model = Post
        #include fields what you want make visible for api
        fields = ['id','title','url','poster','poster_id','created', 'votes']

    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()
    
# serializer for vote - select fileds from model for api
class VoteSerializer(serializers.ModelSerializer):  
    #fields
    class Meta:
        #specify model from models.py
        model = Vote
        #include fields what you want make visible for api
        fields = ['id']
      