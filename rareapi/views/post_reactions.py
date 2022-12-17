'''View module for handeling post reactions'''

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import PostReaction, Post, Reaction, User

class PostReactionView(ViewSet):
    '''Post_Reaction type views'''
    
    def create(self, request):
        '''handels GET all PR requests'''
        post = Post.objects.get(pk=request.data['post_id'])
        reaction = Reaction.objects.get(pk=request.data['reaction_id'])
        user = User.objects.get(pk=request.data['user_id'])
        
        post_reaction = PostReaction.objects.create(
          post_id = post,
          reaction_id = reaction,
          user_id = user
        )
        
        serializer = PostReactionSerializer(post_reaction)
        
        return Response(serializer.data)
    
    def destroy(self, request, pk):
      '''Delete request for post reaction'''
      post_reaction = PostReaction.objects.get(pk=pk)
      post_reaction.delete()
      
      return Response(None, status=status.HTTP_204_NO_CONTENT)
      

class PostReactionSerializer(serializers.ModelSerializer):
    '''JSON Serializer'''
    class Meta:
      model = PostReaction
      fields = ('id', 'post_id', 'reaction_id', 'user_id')
      depth = 0
        