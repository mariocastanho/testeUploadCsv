"""Estoque URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from website.views import IndexTemplateView
from website.views import ProdutoListView
from website.views import ProdutoUpdateView
from website.views import ProdutoDeleteView
from website.views import ProdutoCreateView

# Importamos a função index() definida no arquivo views.py
from . import views

app_name = 'website'

# urlpatterns a lista de roteamentos de URLs para funções/Views
urlpatterns = [

    # '/'
    path('', 
      IndexTemplateView.as_view(), 
      name="index" # <<< Adicionar
    ),

    # '/produto/cadastrar'
    path('produto/cadastrar', 
      ProdutoCreateView.as_view(), 
      name="cria_produto" # <<< Adicionar
    ),

    # '/produtos'
    path('produtos/', 
      ProdutoListView.as_view(), 
      name="lista_produtos" # <<< Adicionar
    ),

    # '/produto/{pk}'
    path('produto/<pk>', 
      ProdutoUpdateView.as_view(), 
      name="atualiza_produto" # <<< Adicionar
    ),

    # '/produtos/excluir/{pk}'
    path('produto/excluir/<pk>', 
      ProdutoDeleteView.as_view(), 
      name="deleta_produto" # <<< Adicionar
    ),
]
