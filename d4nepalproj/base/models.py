from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Plan(models.Model):
    type = models.CharField(max_length = 200, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    kpi_views = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    chart_views = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    default = models.BooleanField(default=False)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.type)

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    subscription_starttime = models.CharField(max_length=200, null=True, blank=True)
    subscription_endtime = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)
    createdAt = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return str(self.subscription_starttime)

    class Meta:
        get_latest_by = ['createdAt']

class RealData(models.Model):
    year = models.CharField(max_length=200)
    month_no = models.IntegerField()
    quarter = models.CharField(max_length=200)
    year_month = models.CharField(max_length=200)
    month_name = models.CharField(max_length=200)
    week = models.CharField(max_length=200)
    week_ending_mon_sun_dt = models.CharField(max_length=200)
    min_orderdatetime = models.CharField(max_length=200)
    kpi = models.CharField(max_length=200)
    menu_category = models.CharField(max_length=200)
    menu_group = models.CharField(max_length=200)
    menu_item = models.CharField(max_length=200)
    actual = models.DecimalField(max_digits=7, decimal_places=2)