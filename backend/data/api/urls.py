from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import DataViewSet

data_router =  DefaultRouter()
data_router.register(r'data', DataViewSet)

urlpatterns = [
    # Include the URLs registered with data_router
    path('', include(data_router.urls)),
]