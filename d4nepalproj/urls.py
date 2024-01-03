from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/plans/', include('base.urls.plan_urls')),
    path('api/subscriptions/', include('base.urls.subscription_urls')),
    path('api/users/', include('base.urls.user_urls')),
    path('api/datas/', include('base.urls.data_urls')),
]