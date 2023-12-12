from rest_framework import serializers
from .models import Plan
from .models import Subscription


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