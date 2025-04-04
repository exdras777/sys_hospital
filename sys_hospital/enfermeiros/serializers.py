from rest_framework import serializers
from .models import Enfermeiros
from enderecos.serializers import EnderecoSerializer

class EnfermeirosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermeiros
        fields = '__all__'
