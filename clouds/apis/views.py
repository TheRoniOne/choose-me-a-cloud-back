from rest_framework.viewsets import ModelViewSet

from clouds.apis.serializers import CloudSerializer
from clouds.models import Cloud


class CloudViewSet(ModelViewSet):
    queryset = Cloud.objects.all()
    serializer_class = CloudSerializer
