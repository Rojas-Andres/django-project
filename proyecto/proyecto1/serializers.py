from rest_framework import serializers
from .models import Enterprise,Code


#El serializador es como se debe de armar el json que se va a usar en viewsets
class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = '__all__'


class CodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Code
        fields = '__all__'
    