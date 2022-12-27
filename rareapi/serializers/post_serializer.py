from rest_framework import serializers, status
from rareapi.models import Post

class PostSerializer(serializers.ModelSerializer):
      """JSON serializer for posts"""
      
      class Meta:
          model = Post
          fields = ('id', 'user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content', 'approved', 'tags_on_posts', 'edited_on')
          depth = 1    
