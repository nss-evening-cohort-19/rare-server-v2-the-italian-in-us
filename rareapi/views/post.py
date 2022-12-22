"""View module for handling requests concerning posts"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, User, Category

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
        category = Category.objects.get(pk=request.data['category_id'])
        
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
        post.edited_on = request.data['edited_on']
        post.title = request.data['title']
        post.image_url = request.data['image_url']
        post.content = request.data['content']
        
        post.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
class PostSerializer(serializers.ModelSerializer):
      """JSON serializer for posts"""
      
      class Meta:
          model = Post
          fields = ('id', 'user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content', 'approved', 'edited_on')
          depth = 1         
