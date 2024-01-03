from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from base.models import Plan
from base.serializers import PlanSerializer
from rest_framework import generics


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