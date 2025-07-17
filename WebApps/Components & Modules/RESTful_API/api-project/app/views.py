from django.shortcuts import render
from rest_framework import generics,permissions, mixins, status
from rest_framework.exceptions import ValidationError
from .models import Post, Vote, User
from .serializers import PostSerializer, VoteSerializer
from rest_framework.response import Response

# Token Implementation
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
#every user to have an automatically generated Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.get_or_create(user=instance)
 
# Api views here to read (get method) the post only.
"""class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer"""

# create a Class to read all posts (get method) and create the post (post method).
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    #grand permision to read and create posts  to registerd user only
    #permission_classes = [permissions.IsAuthenticated]
    
    #grand permision to read posts  to ALL users, but create to registered only
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Generate POSTER _ID automaticly
    def perform_create (self,serializer):
        serializer.save (poster=self.request.user)

# create a Class to read-delete ONE post 
class PostRetriveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #grand permision to read/delete post 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# function which lets user delete a particular post
    def delete(self, request, *args, **kwargs):
        post = Post.objects.filter(pk=self.kwargs['pk'], poster = self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('This is not your post, you can not delete it.')
         

# create a Class to lets users to vote
class VoteCreate(generics.CreateAPIView,mixins.DestroyModelMixin):
    serializer_class = VoteSerializer

    #grand permision to vote for registered users only
    permission_classes = [permissions.IsAuthenticated]
    
    # function control that voting for particular user and post
    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user,post=post)
    
    def perform_create (self,serializer):
        #serializer.save(voter=self.request.user, post=Post.objects.get(pk=self.kwargs['pk']))
        
        # function control that voting for particular user and post happens only once!
        if self.get_queryset().exists():
            raise ValidationError('You have already voted for this post')
        serializer.save(voter=self.request.user, post=Post.objects.get(pk=self.kwargs['pk']))
    
    # function which lets user delete a particular vote
    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('You never voted for this post :(')
            







