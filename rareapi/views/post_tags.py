from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, Tags, PostTags

class PostTagsView(ViewSet):
    """Rare PostTags View"""

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized post instance
        """
        tag = Tags.objects.get(pk=request.data['tag_id'])
        post = Post.objects.get(pk=request.data['post_id'])
        
        post_tag = PostTags.objects.create(
          tag = tag,
          post = post
        )
        
        serializer = PostTagsSerializer(post_tag)
        return Response(serializer.data)

    def destroy(self, request, pk):
        post_tag = PostTags.objects.get(pk=pk)
        post_tag.delete()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
class PostTagsSerializer(serializers.ModelSerializer):
      """JSON serializer for categories"""
      
      class Meta:
          model = PostTags
          fields = ('id', 'tag', 'post')
          depth = 1
