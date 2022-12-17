'''category module for get only'''

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Reaction

class ReactionView(ViewSet):
    '''Category type view'''
    
    def list(self, request):
      '''handels GET all request'''
      
      reactions = Reaction.objects.all()
      
      serializer = ReactionSerializer(reactions, many=True)
      react_serialized = serializer.data
      for reaction in react_serialized:
        reaction['imageUrl'] = reaction.pop('image_url')      
      
      return Response(react_serialized)
    
    def create(rels, request): 
      '''handels create reaction'''
      reaction = Reaction.objects.create(
        label = request.data['label'],
        image_url = request.data['imageUrl']
      )
      serializer = ReactionSerializer(reaction)
      react_serialized = serializer.data
      react_serialized['imageUrl'] = react_serialized.pop('image_url')
      
      return Response(react_serialized)
    
    def destroy(self, request, pk):
      '''Handels Delete Request for Reactions'''
      reaction = Reaction.objects.get(pk=pk)
      reaction.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
      
class ReactionSerializer(serializers.ModelSerializer):
    '''JSON Serializer'''
    class Meta:
      model = Reaction
      fields = ('id', 'label', 'image_url')
