from rest_framework.viewsets import ModelViewSet
from data.models import Data
from .serializers import DataSerializer


class DataViewSet(ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer