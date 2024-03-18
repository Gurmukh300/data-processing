from rest_framework.viewsets import ModelViewSet
from ..models import Data
from .serializers import DataSerializer


class DataViewSet(ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer