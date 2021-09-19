from website.models import Produto
from django import forms

class InsereProdutoForm(forms.ModelForm):
  class Meta:
    # Modelo base
    model = Produto

    # Campos que estarão no form
    fields = [
      'produto',
      'descricao',
      'preco_venda'
    ]
