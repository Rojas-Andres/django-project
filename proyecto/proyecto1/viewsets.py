from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.response import Response

from django.views.generic.edit  import CreateView


class EnterpriseViewset(viewsets.ModelViewSet):
    queryset = models.Enterprise.objects.all()
    serializer_class = serializers.EnterpriseSerializer

class CodeViewset(viewsets.ModelViewSet):
    queryset = models.Code.objects.all()
    serializer_class = serializers.CodeSerializer
