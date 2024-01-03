from django.urls import path
from base.views import subscription_views as views

urlpatterns = [
    path('subscriptions-create/<str:pk>', views.createSubscription, name="subscription-create"),
    path('<str:pk>/subscriptions-update/<str:plan_id>/', views.updatetSubscription, name="subscription-update"),
    path('index', views.getSubscriptions, name="subscriptions"),
    path('<str:pk>', views.getSubscription, name="subscription"),
    # path('update', views.updateSub, name="update-subscription")
]