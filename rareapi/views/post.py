"""View module for handling requests concerning posts"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from rareapi.models import Post, User, Category,PostTags, Tags
from rareapi.views.tags import TagsSerializer
from rest_framework.decorators import action
from rareapi.views.user import UserSerializer
from rareapi.serializers import PostSerializer


class PostView(ViewSet):
    """Rare Post View"""
     
    def retrieve(self, request, pk):
        """Handle GET requests from single post
        Returns:
            Response -- JSON serialized post
        """
        try:
            post = Post.objects.get(pk=pk)
        
            filtered_post_tags = PostTags.objects.filter(post=post.id)
            tags_on_posts = []
            
            for post_tag_obj in filtered_post_tags:
                try:
                    tags_on_post = Tags.objects.get(id=post_tag_obj.tag_id)

                    tags_on_posts.append(tags_on_post.label)
                except:
                    pass
            post.tags_on_posts = tags_on_posts

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
        
        for post in posts:
            filtered_post_tags = PostTags.objects.filter(post=post.id)
            tags_on_posts = []
            
            for post_tag_obj in filtered_post_tags:
                try:
                    tags_on_post = Tags.objects.get(id=post_tag_obj.tag_id)
                    tags_on_posts.append(tags_on_post.label)
                except:
                    pass
            post.tags_on_posts = tags_on_posts
            
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
        
        #capture post tags from form and create them
        tag_ids = request.data['tag_ids']
        
        tags = [Tags.objects.get(pk=tag_id) for tag_id in tag_ids]
        
        for tag in tags:
            post_tag = PostTags(post=post, tag=tag)
            post_tag.save()
        
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
    
    @action(methods=['get'], detail=True)
    def getSubscribedPosts(self, request, pk):
        """Get user custom feed based on subscriptions"""
        user = User.objects.get(pk=pk)
        follower_ids = [user['author_id'] for user in user.following]
        follower_list = [User.objects.get(pk=id) for id in follower_ids]
        follower_serialized = UserSerializer(follower_list, many=True)
        posts = [post for user in follower_serialized.data for post in user['posts']]
        instances = [Post.objects.get(pk=post['user_id']) for post in posts]
        serialized = PostSerializer(instances, many=True)
        
        return Response(serialized.data)

        
        
        