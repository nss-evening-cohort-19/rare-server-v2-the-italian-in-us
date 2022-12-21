from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import User, Subscription
from .subscriptions import SubscriptionSerializer

class UserView(ViewSet):
  
  def retrieve(self, request, pk):
    
    user = User.objects.get(pk=pk)
    
    uid = request.META['HTTP_AUTHORIZATION']
    logged_in_user = User.objects.get(uid=uid)
    user.subbed = any(sub['follower_id'] == logged_in_user.id for sub in user.subscribers)
    
    serializer = UserSerializer(user)
    
    return Response(serializer.data)
    
  

class UserSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = User
    fields = ('id', 'uid', 'first_name', 'last_name', 'bio', 'email', 'created_on', 'active', 'is_staff', 'profile_image_url', 'email', 'subscribers', 'posts', 'following', 'subbed')
