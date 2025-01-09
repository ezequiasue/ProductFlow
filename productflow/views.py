# Create your views here.
from django.shortcuts import render, redirect
from .models import Categoria, Fornecedor, Produto


def index(request):
    return render(request, 'index.html')  # Certifique-se de que o arquivo index.html está na pasta templates

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listar.html', {'categorias': categorias})

# View para criar categoria sem usar ModelForm
def criar_categoria(request):
    if request.method == 'POST':
        nome_categoria = request.POST.get('nome')
        
        if nome_categoria:
            # Cria e salva a nova categoria no banco de dados
            categoria = Categoria(nome=nome_categoria)
            categoria.save()
            return redirect('listar_categorias')  # Redireciona para a lista de categorias
    return render(request, 'categorias/criar.html')
