from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    perfil = Perfil()

    if perfil_id == 1:
        perfil = Perfil('Thaís Carvalho', 'thais@email.com', '12345532', 'Eldorado')
    if perfil_id == 2:
        perfil = Perfil('Gabriel Fernandes', 'gabriel@email.com', '23554321', 'CFA')
    return render(request, 'perfil.html', {'perfil': perfil})