from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Tags

class TagsView(ViewSet):
    """rareapi tags view"""
  
    def retrieve(self, request, pk):
        """Handle GET requests for single tag type

        Returns:
            Response -- JSON serialized tag type
        """
        try:
          tag = Tags.objects.get(pk=pk)
          serializer = TagsSerializer(tag)
          return Response(serializer.data)
        except Tags.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all tag types

        Returns:
            Response -- JSON serialized list of tag types
        """
        
        tags = Tags.objects.all()
        serializer = TagsSerializer(tags, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized tag instance
        """
        tag = Tags.objects.create(
          label=request.data["label"]
        )
        serializer = TagsSerializer(tag)
        return Response(serializer.data)
      
    def update(self, request, pk):
        """Handle PUT requests to get all tags

        Returns:
            Response -- 204
        """
        tag = Tags.objects.get(pk=pk)
        tag.label = request.data['label']
        tag.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)
      
    def destroy(self, request, pk):
        tag = Tags.objects.get(pk=pk)
        tag.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
class TagsSerializer(serializers.ModelSerializer):
    """JSON serializer for tags
    """
    class Meta:
        model = Tags
        fields = ('id', 'label')
