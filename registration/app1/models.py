from django.db import models
import datetime
from django.contrib.auth.models import User



def fk(model):
    return models.ForeignKey(model, on_delete=models.CASCADE)


class Porta(models.Model):

    utilizador = fk(User)
    registo_hora = models.DateTimeField(default=datetime.datetime.now())

