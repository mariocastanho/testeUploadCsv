from website.models import Estoque
from website.models import Produto
from django.urls import path, reverse_lazy
from django.shortcuts import redirect, render
from django.db import models
from django.contrib import admin
from django import forms
from django.http import HttpResponse
from django.http import JsonResponse

# Register your models here.

class CsvImportForm(forms.Form):
    csv_estoque_upload = forms.FileField()

#class CadastroProdutosCsvForm(forms.Form):
#    cadastro_novos_produtos = forms.CharField

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'estoque', 'produto', 'quantidade')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls
    
    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_estoque_upload"]
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            produtos_novos = []

            for x in csv_data:
                if x != "":
                    fields = x.split(",")
                    objeto_produto_csv = Produto.objects.filter(produto=fields[1])
                    
                    if not objeto_produto_csv:
                        produtos_novos.append(fields[1])

            if len(produtos_novos) == 0:
                for x in csv_data:
                    if x != "":
                        fields = x.split(",")
                        objeto_produto_csv = Produto.objects.get(produto=fields[1])
                        created = Estoque.objects.create(
                            estoque = fields[0],
                            produto = objeto_produto_csv,
                            quantidade = fields[2],                    
                        )
                return redirect("/admin/website/estoque")
            else:
                produtos = {"produtos": produtos_novos}
                return render(request, 'admin/cadastro_novos_produtos.html', produtos)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_estoque_upload.html", data)



class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'preco_venda', 'descricao')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('cadastro-novos-produtos/', self.cadastro_novos_produtos),]
        return new_urls + urls

    def cadastro_novos_produtos(self, request):
        if request.method == "POST":
            array_produtos = request.POST.getlist('array_produtos[]')
            if len(array_produtos) > 0:
                for x in array_produtos:
                    if x[0] != "":
                        a = x.split(",")
                        created = Produto.objects.create(
                            produto = a[0],
                            preco_venda = a[1],
                            descricao = a[2],                    
                        )
                return JsonResponse({'HTTPRESPONSE':1})

admin.site.register(Estoque, EstoqueAdmin)
admin.site.register(Produto, ProdutoAdmin)