from django.db import models

# Create your models here.
class Produto(models.Model):
    def __str__(self):
        return self.produto

    produto = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )

    preco_venda = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )

    descricao = models.TextField(
        null=False,
        blank=False
    )

class Estoque(models.Model):
    def __str__(self):
        return self.estoque
        
    estoque = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    produto = models.ForeignKey("Produto",on_delete=models.DO_NOTHING)

    quantidade = models.IntegerField(
        null=False,
        blank=False
    )

