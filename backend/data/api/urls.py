from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import DataViewSet

data_router =  DefaultRouter()
data_router.register(r'data', DataViewSet)