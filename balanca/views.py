from django.shortcuts import render
from django.http import JsonResponse
from .models import Pesagem

def listar_pesos(request):
    pesos = list(Pesagem.objects.all())
    return JsonResponse(pesos, safe = False)

