from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response

from base.models import Subscription,Plan
from base.serializers import SubscriptionSerializer
from rest_framework import generics

@api_view(['GET'])
def getSubscriptions(request):
    subscriptions = Subscription.objects.all()
    serializer = SubscriptionSerializer(subscriptions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSubscription(request, pk):
    subscription = Subscription.objects.get(_id=pk)
    serializer = SubscriptionSerializer(subscription, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createSubscription(request, pk):
    data = request.data
    plan = Plan.objects.get(_id=pk)
    user = request.user
    subscription = Subscription.objects.create(
      plan = plan,
      user = user,
      subscription_starttime=data['subscription_starttime'],
      subscription_endtime=data['subscription_endtime']
    )
    serializer = SubscriptionSerializer(subscription, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updatetSubscription(request, pk, plan_id):
    data = request.data
    plan = Plan.objects.get(_id=plan_id)
    user = request.user
    subscription = Subscription.objects.get(_id=pk)
    subscription.plan = plan
    subscription.subscription_starttime = data['subscription_starttime']
    subscription.subscription_endtime = data['subscription_endtime']
    subscription.save()
    serializer = SubscriptionSerializer(subscription, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def updateSub(request):
    return "hello"