from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/criar/', views.criar_categoria, name='criar_categoria'),
    path('fornecedores/', views.lista_fornecedores, name='lista_fornecedores'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),
]
