from django.urls import path
from base.views import plan_views as views
from base.views import subscription_views as subscriptionViews

urlpatterns = [
    path('plans-create/', views.createPlan, name="plan-create"),
    path('<str:pk>/subscribe', subscriptionViews.createSubscription, name="subscription-create"),
    path('index', views.getPlans, name="plans"),
    path('<str:pk>', views.getPlan, name="plan"),
]