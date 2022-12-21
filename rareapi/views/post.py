"""View module for handling requests concerning posts"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from rareapi.models import Post, User, Category,PostTags, Tags

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
        
    def list(self, request):
        """Handle GET requests to get all posts

        Returns:
            Response -- JSON serialized list of posts
        """
        posts = Post.objects.all()
        
        category_of_posts = request.query_params.get('category', None)
        if category_of_posts is not None:
            posts = posts.filter(category_id=category_of_posts)
        
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized post instance
        """
        user = User.objects.get(uid=request.data['uid'])
        category = Category.objects.get(pk=request.data['category'])
        
        post = Post.objects.create(
            title=request.data['title'],
            publication_date=request.data['publication_date'],
            image_url=request.data['image_url'],
            content=request.data['content'],
            approved=True,
            user_id=user,
            category_id=category
        )
        
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a post

        Returns:
            Response -- Empty body with 204 status code
        """
        
        post = Post.objects.get(pk=pk)
        post.title = request.data['title']
        post.publication_date = request.data['publication_date']
        post.image_url = request.data['image_url']
        post.content = request.data['content']
        
        post.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    @action(methods=['post'], detail=True)
    def add_tag(self, request, pk):
        tag = Tags.objects.get(pk=request.data['id'])
        post = Post.objects.get(pk=pk)
        
        PostTags.objects.create(
            tag = tag,
            post = post
        )
        return Response({'message': 'Tag Added to Post'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def remove_tag(self, request, pk):
        tag = Tags.objects.get(pk=request.data['id'])
        post = Post.objects.get(pk=pk)
        
        post_tag = PostTags.objects.create(
            tag = tag,
            post = post
        )
        post_tag.delete()
        return Response({'message': 'Tag Removed from Post'}, status=status.HTTP_201_CREATED)
class PostSerializer(serializers.ModelSerializer):
      """JSON serializer for posts"""
      
      class Meta:
          model = Post
          fields = ('id', 'user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content', 'approved', 'tags_on_posts')
          depth = 1        
