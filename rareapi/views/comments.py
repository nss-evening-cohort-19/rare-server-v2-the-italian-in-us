'''Comments module for request handeling'''

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Comment, Post, User
from rest_framework.decorators import action

class CommentView(ViewSet):
    '''Comment View'''
    def retrieve(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        
        serializer = CommentSerializer(comment)
        serial_comment = serializer.data
        serial_comment['createdOn'] = serial_comment.pop('created_on')
        serial_comment['authorId'] = serial_comment.pop('author_id')
        serial_comment['postId'] = serial_comment.pop('post_id')
        
        return Response(serial_comment)
    
    def list(self, request):
      '''handels list by post id'''
      comments = Comment.objects.all()
      
      post_id = request.query_params.get('postId', None)
      if post_id is not None:
        comments = comments.filter(post_id = post_id)
      
      serializer = CommentSerializer(comments, many=True)
      serial_comment = serializer.data
      for comment in serial_comment:
        comment['createdOn'] = comment.pop('created_on')
        comment['authorId'] = comment.pop('author_id')
        comment['postId'] = comment.pop('post_id')
    
      return Response(serial_comment)
           
      
    def create(self, request):
        '''handels creation of post comment'''
        post = Post.objects.get(pk=request.data['postId'])
        author = User.objects.get(pk=request.data['authorId'])
        
        comment = Comment.objects.create(
          post_id = post,
          author_id = author,
          content = request.data['content'],
          created_on = request.data['createdOn']
        )
        
        serializer = CommentSerializer(comment)
        
        return Response(serializer.data)
    
    def update(self, request, pk):
        '''handels update request for coments'''
        comment = Comment.objects.get(pk=pk)
        comment.content = request.data['content']
        
        comment.save()
        
        serializer = CommentSerializer(comment)
        
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        '''handels delete request for comments'''
      
        comment = Comment.objects.get(pk=pk)
        comment.delete()
      
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
        
class CommentSerializer(serializers.ModelSerializer):
  '''JSON Serializer'''
  class Meta:
    model= Comment
    fields= ('id', 'author_id', 'content', 'created_on', 'post_id')
    depth = 1
        
 