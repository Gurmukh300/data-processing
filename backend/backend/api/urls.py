from rest_framework.routers import DefaultRouter
from data.api.urls import data_router
from django.urls import path, include

router = DefaultRouter()

router.registry.extend(data_router.registry)

urlpatterns = [
    path('', include(router.urls))
]