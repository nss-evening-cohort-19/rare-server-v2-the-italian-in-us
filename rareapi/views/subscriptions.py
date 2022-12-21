from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import User, Subscription


class SubscriptionView(ViewSet):
  """handles all requests for subscriptions"""
  
  def list(self, request):
    """handles GET requests for subscriptions"""
    subs = Subscription.objects.all()
    
    serializer = SubscriptionSerializer(subs, many=True)
    return Response(serializer.data)
    
  def destroy(self, request, pk):
    sub = Subscription.objects.get(pk=pk)
    sub.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
    
  def create(self, request):
    """handles POST requests for subscriptions"""
    follower = User.objects.get(pk=request.data['follower_id'])
    author = User.objects.get(pk=request.data['author_id'])
    
    sub = Subscription.objects.create(
      follower_id = follower,
      author_id = author,
      created_on = request.data['created_on']
    )
    
    serializer = SubscriptionSerializer(sub)
    
    return Response(serializer.data)
    
    
class SubscriptionSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Subscription
    fields =('id', 'follower_id', 'author_id', 'created_on')
