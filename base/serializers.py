from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.timezone import now
from rest_framework import serializers
from .models import Plan
from .models import Subscription
from .models import DummyData
from django.db import models


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()
    class Meta:
        model = Subscription
        fields = '__all__'

    def get__id(self, obj): 
        return obj.id
      
class UserSerializer(serializers.ModelSerializer):
    subscriptions = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id','_id','username','email','name','isAdmin','subscriptions']
        # fields = '__all__'

    def get__id(self, obj): 
        return obj.id

    def get_isAdmin(self, obj): 
        return obj.is_staff

    def get_name(self, obj):
        return obj.email if not obj.first_name else obj.first_name

    def get_subscriptions(self, obj):
        try:
            subscriptions = obj.subscription_set.latest()
            serializer = SubscriptionSerializer(subscriptions, many=False)
            return serializer.data
        except Exception as e:
            return None

class UserSerializerWithToken(UserSerializer):
    subscriptions = serializers.SerializerMethodField(read_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','_id','username','email','name','isAdmin','token','subscriptions']
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

    def get_subscriptions(self, obj):
        try:
            subscriptions = obj.subscription_set.latest()
            serializer = SubscriptionSerializer(subscriptions, many=False)
            return serializer.data
        except Exception as e:
            return None

class DummyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DummyData
        fields = ['kpi','actual']
        # fields = '__all__'