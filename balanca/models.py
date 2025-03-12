from django.db import models

class Pesagem(models.Model):
    peso = models.FloatField()
    data_hora = models.DateTimeField(auto_now_add = True)

def __str__(self):
    return f"{self.peso}kg em {self.data_hora}"