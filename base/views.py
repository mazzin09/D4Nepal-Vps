from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Plan
from base.serializers import PlanSerializer

from base.models import Subscription
from base.serializers import SubscriptionSerializer


# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    return JsonResponse('Hello', safe=False)


#PLAN VIEW
@api_view(['GET'])
def getPlans(request):
    plans = Plan.objects.all()
    serializer = PlanSerializer(plans, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPlan(request, pk):
    plan = Plan.objects.get(_id=pk)
    serializer = PlanSerializer(plan, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createPlan(request):
    data = request.data
    
    plan = Plan.objects.create(
        type=data['type'],
        price=data['price'],
        kpi_views=data['kpi_views'],
        chart_views=data['chart_views'],
        default=data['default'],
    )
    serializer = PlanSerializer(plan, many=False)
    return Response(serializer.data)


# SUBSCRIPTION VIEW
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