from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import CreateView
from website.models import Produto
from website.forms import InsereProdutoForm


# Create your views here.
class IndexTemplateView(TemplateView):
  template_name = "website/index.html"

class ProdutoListView(ListView):
  template_name = "website/lista_produtos.html"
  model = Produto
  context_object_name = "produtos"

class ProdutoUpdateView(UpdateView):
  template_name = "website/atualiza_produto.html"
  model = Produto
  fields = '__all__'
  context_object_name = 'produto'

  def get_object(self, queryset=None):
    produto = None

    # Se você utilizar o debug, verá que os 
    # campos {pk} e {slug} estão presente em self.kwargs
    id = self.kwargs.get(self.pk_url_kwarg)
    slug = self.kwargs.get(self.slug_url_kwarg)

    if id is not None:
      # Busca o funcionario apartir do id
      produto = Produto.objects.filter(id=id).first()

    elif slug is not None:        
      # Pega o campo slug do Model
      campo_slug = self.get_slug_field()

      # Busca o produto apartir do slug
      produto = Produto.objects.filter(**{campo_slug: slug}).first()

    # Retorna o objeto encontrado
    return produto

class ProdutoDeleteView(DeleteView):
  template_name = "website/exclui_produto.html"
  model = Produto
  context_object_name = 'produto'
  success_url = reverse_lazy("website:lista_produtos")

class ProdutoCreateView(CreateView):
  template_name = "website/cria_produto.html"
  model = Produto
  form_class = InsereProdutoForm
  success_url = reverse_lazy("website:lista_produtos")
