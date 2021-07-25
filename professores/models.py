from django.db import models
from django.forms.fields import CharField

# Create your models here.
#Professor = None
class Professor(models.Model):
    nome_professor = models.CharField(max_length=60)
    formacao = models.CharField(max_length=25)
    tempo_de_experiencia_em_anos = models.CharField(max_length=3)
    area_de_atuacao = models.CharField(max_length=140)

    def __str__(self):
        return self.nome_professor