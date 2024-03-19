# from rest_framework.routers import DefaultRouter
# from data.api.urls import data_router
# from django.urls import path, include

# router = DefaultRouter()

# router.registry.extend(data_router.registry)

# urlpatterns = [
#     path('', include(router.urls))
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from data.api.views import DataViewSet
from data.api.urls import data_router
# Define the router and register the DataViewSet
router = DefaultRouter()
router.registry.extend(data_router.registry)

# Other URL patterns...
urlpatterns = [
    # Include the URLs registered with data_router
    path('', include(router.urls)),
    
    # URL pattern for uploading CSV
    path('api/data/upload_csv/', DataViewSet.as_view({'post': 'upload_csv'}), name='upload_csv'),
]
