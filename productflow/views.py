from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Fornecedor, Produto

def index(request):
    return render(request, 'index.html')

def criar_categoria(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        if nome:
            Categoria.objects.create(nome=nome)
            return redirect("lista_categorias")  # Redireciona para a lista de categorias

    return render(request, "categorias/criar.html")

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listar.html', {'categorias': categorias})



def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores/listar.html', {'fornecedores': fornecedores})

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar.html', {'produtos': produtos})

def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produtos/detalhe_produto.html', {'produto': produto})
