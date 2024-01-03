from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from base.models import User
from base.serializers import UserSerializer, UserSerializerWithToken

from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework import generics


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k,v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
 
# class SalesListView(generics.ListAPIView):
#     serializer_class = SalesSerializer

#     def get_queryset(self):
#         kpi = self.request.query_params.get('kpi', None)
#         if kpi is not None:
#             # Use Sum function to sum the values of the "Actual" field for both filters
#             total_sales = DummyData.objects.filter(KPI='Total Sales').aggregate(total_sales=Sum('Actual'))
#             total_tax = DummyData.objects.filter(KPI='Total Sales Tax').aggregate(total_tax=Sum('Actual'))
#             # Combine the results into a single dictionary
#             queryset = {total_sales, total_tax}
#             serializer = SalesSerializer(queryset, many=True)
#             return serializer.data
#         else:
#             queryset = DummyData.objects.all()
#             return queryset


# Create your views here.

# Register code
@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except Exception as e:
        message = e
        return Response(message, status=status.HTTP_400_BAD_REQUEST,template_name=None,content_type=None)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

