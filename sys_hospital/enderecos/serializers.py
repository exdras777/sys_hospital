from rest_framework import serializers
from .models import Endereco


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

"""
from rest_framework import serializers
from .models import Paciente
from enderecos.serializers import EnderecoSerializer

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
    model = Paciente
    fields = '__all__'

"""