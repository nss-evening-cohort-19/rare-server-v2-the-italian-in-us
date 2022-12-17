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
    
  def retrieve(self, request, pk):
    """handles single Subscription get"""
    
    
    
    
class SubscriptionSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Subscription
    fields =('id', 'follower_id', 'author_id', 'created_on', 'ended_on')
