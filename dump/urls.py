from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes, name="Routes"),
    # PLAN URL
    path('plan/index', views.getPlans, name="plans"),
    path('plan/create', views.createPlan, name="plan-create"),
    path('plan/<str:pk>', views.getPlan, name="plan"),

    # SUBSCRIPTION URL
    path('subscriptions-create/', views.createSubscription, name="subscription-create"),
    path('subscription/index', views.getSubscriptions, name="subscriptions"),
    path('subscription/<str:pk>', views.getSubscription, name="subscription"),

]