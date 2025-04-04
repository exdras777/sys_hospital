from django.db import models

class Doencas(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=200)
    sintomas = models.CharField(max_length=110, unique=True)
    tratamentos = models.CharField(max_length=110, unique=True)  # Chave estrangeira para Endereco
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'doencas'

    def __str__(self):
        return self.nome
