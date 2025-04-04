from django.db import models
from enderecos.models import Endereco  # Importa o modelo Endereco
from especializacoes.models import Especializacoes  # Importa o modelo Endereco

class Medicos(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    crm = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)  # Chave estrangeira para Endereco
    especializacao = models.ForeignKey(Especializacoes, on_delete=models.CASCADE)  # Chave estrangeira para Endereco
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)  # Timestamp automático na criação
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'medicos'

    def __str__(self):
        return self.nome
