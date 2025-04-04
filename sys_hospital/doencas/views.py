from rest_framework import viewsets, permissions
from .models import Doencas
from .serializers import DoencasSerializer

class DoencasViewSet(viewsets.ModelViewSet):
    queryset = Doencas.objects.all()
    serializer_class = DoencasSerializer
    permission_classes = [permissions.AllowAny]  # Permite qualquer acesso (para testes)