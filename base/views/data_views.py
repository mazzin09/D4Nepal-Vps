from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response

from base.models import DummyData
from base.serializers import DummyDataSerializer

from rest_framework import status

from rest_framework import generics
from django.db.models import Q, Sum, Count


def sales_list(request):
    queryset = DummyData.objects.filter(kpi='Total Sales').aggregate(total_sales=Sum('actual'))
    serializer = DummyDataSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False) 
    
@api_view(['GET'])
def showData(request):
    def get_data(filter_query):
        totalSales = DummyData.objects.filter(filter_query, Q(kpi="Total Sales")).aggregate(Sum('actual'))['actual__sum']
        totalVoid = DummyData.objects.filter(filter_query, Q(kpi="Total Void Amount")).aggregate(Sum('actual'))['actual__sum']
        totalGuestCount = DummyData.objects.filter(filter_query, Q(kpi="Total Guest Count")).count()
        totalOrderCount = DummyData.objects.filter(filter_query, Q(kpi="Total Order Count")).count()
        food = DummyData.objects.values('month_name', 'menu_category').filter(filter_query).annotate(total_sales=Sum('actual')).values('month_name', 'menu_category', 'total_sales', 'quarter')
        group = DummyData.objects.values('month_name', 'menu_group').filter(filter_query).annotate(total_sales=Sum('actual')).values('month_name', 'menu_group', 'total_sales', 'quarter')
        item = DummyData.objects.values('month_name', 'menu_item').filter(filter_query).annotate(total_sales=Sum('actual')).values('month_name', 'menu_item', 'total_sales', 'quarter')

        result = {}
        for sale in food:
            month = sale['month_name']
            if month not in result:
                result[month] = {'month': month, sale['menu_category']: sale['total_sales'], 'quarter': sale['quarter']}
            else:
                result[month][sale['menu_category']] = sale['total_sales']

        groupResult = {}
        for sale in group:
            month = sale['month_name']
            if month not in groupResult:
                groupResult[month] = {'month': month, sale['menu_group']: sale['total_sales']}
            else:
                groupResult[month][sale['menu_group']] = sale['total_sales']

        return {
            'totalSales': totalSales,
            'totalVoid': totalVoid,
            'totalGuestCount': totalGuestCount,
            'totalOrderCount': totalOrderCount,
            'result': result,
            'groupResult': groupResult,
            'item': item
        }

    query_param = request.query_params.get('by_qtr')
    filter_query = Q(quarter='Q1') | Q(quarter='Q2') | Q(quarter='Q3') | Q(quarter='Q4')

    match query_param:
        case 'q2':
            filter_query = Q(quarter='Q1') | Q(quarter='Q2')
            data = get_data(filter_query)
        case 'q3':
            filter_query = Q(quarter='Q1') | Q(quarter='Q2') | Q(quarter='Q3')
            data = get_data(filter_query)
        case 'q4':
            filter_query = Q(quarter='Q1') | Q(quarter='Q2') | Q(quarter='Q3') | Q(quarter='Q4')
            data = get_data(filter_query)
        case _:
            data = get_data(Q(quarter='Q1'))

    return Response({
        "kpi": {
            "sales_sum": {'title': "Total Sales", 'value': round(data['totalSales'], 2)},
            "void_sum": {'title': "Total Void Sales", 'value': round(data['totalVoid'], 2)},
            "guest_count": {'title': "Total Guest Count", 'value': data['totalGuestCount']},
            "order_count": {'title': "Total Order Count", 'value': data['totalOrderCount']},
        },
        "chart": data['result'],
        "item": data['item'],
        "group": data['groupResult'],
    })

