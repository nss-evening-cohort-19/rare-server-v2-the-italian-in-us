"""View module for handling requests concerning posts"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post

class PostView(ViewSet):
    """Rare Post View"""
     
    def retrieve(self, request, pk):
        """Handle GET requests from single post
        Returns:
            Response -- JSON serialized post
        """
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
class PostSerializer(serializers.ModelSerializer):
      """JSON serializer for posts"""
      
      class Meta:
          model = Post
          fields = ('id', 'user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content', 'approved')
          depth = 1         
