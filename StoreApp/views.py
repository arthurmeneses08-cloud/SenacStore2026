from django.shortcuts import render
from StoreApp.models import Departamento, Produto

# Create your views here.
def index(request):
    #
    departamento = Departamento.objects.all()
    produtos = Produto.objects.all()


    context = {
        'departamento': departamento,
        'produtos': produtos
    }

    return render(request, 'index.html', context)

def produtos(request):
   

    context = {}

    return render(request, 'produtos.html', context)

