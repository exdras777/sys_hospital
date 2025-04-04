from rest_framework import viewsets, permissions
from .models import Especializacoes
from .serializers import EspecializacoesSerializer

class EspecializacoesViewSet(viewsets.ModelViewSet):
    queryset = Especializacoes.objects.all()
    serializer_class = EspecializacoesSerializer
    permission_classes = [permissions.AllowAny]  # Permite qualquer acesso (para testes)