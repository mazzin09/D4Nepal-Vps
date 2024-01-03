from django.urls import path
from base.views import data_views as views

urlpatterns = [
   path('data/', views.showData, name='data'),
   ]