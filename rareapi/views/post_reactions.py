'''View module for handeling post reactions'''

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import PostReaction, Post, Reaction, User

class PostReactionView(ViewSet):
    '''Post_Reaction type views'''
    
    def list(self, request):
        '''handels GET ALL PR requests'''
        post_reactions = PostReaction.objects.all()
        
        post_id = request.query_params.get('postId', None)
        reaction_id = request.query_params.get('id', None)
        user_id = request.query_params.get('userId', None)
        
        if post_id and reaction_id and user_id is not None:
          post_reactions = post_reactions.filter(post_id = post_id, reaction_id = reaction_id, user_id = user_id)
        
        # if post_id is not None:
        #   post_reactions = post_reactions.filter(post_id = post_id)
        
        serializer = PostReactionSerializer(post_reactions, many=True)
        post_reactions_serialized = serializer.data
        for postReaction in post_reactions_serialized:
          postReaction['postId'] = postReaction.pop('post_id')
          postReaction['reactionId'] = postReaction.pop('reaction_id')
          postReaction['userId'] = postReaction.pop('user_id')
        
        return Response(post_reactions_serialized)
        
        
    def create(self, request):
        '''handels POST PR requests'''
        post = Post.objects.get(pk=request.data['postId'])
        reaction = Reaction.objects.get(pk=request.data['reactionId'])
        user = User.objects.get(pk=request.data['userId'])
        
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
        