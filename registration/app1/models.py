from django.db import models
import datetime
from django.contrib.auth.models import User



def fk(model):
    return models.ForeignKey(model, on_delete=models.CASCADE)


class Porta(models.Model):

    utilizador = fk(User)
    registo_hora = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.utilizador.username} --> {self.registo_hora}"


class Mensagem(models.Model):

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    texto = models.TextField()

    def __str__(self) -> str:
        return f"{self.nome} --> {self.email}"


