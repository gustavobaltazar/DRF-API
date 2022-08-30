from dataclasses import fields
from decimal import Decimal
from rest_framework import serializers
from loja.models import Produto

# class ProdutoSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     titulo = serializers.CharField(max_length=255)
#     preco = serializers.DecimalField(max_digits=6, decimal_places=2)
#     preco_taxado = serializers.SerializerMethodField(method_name='calcular_taxa')

#     def calcular_taxa(self, produto : Produto):
#         return produto.preco * Decimal(1.1)

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'titulo', 'preco', 'preco_taxado', 'estoque', 'categoria']

    preco_taxado = serializers.SerializerMethodField(method_name='calcular_taxa')

    def calcular_taxa(self, produto : Produto):
        return produto.preco * Decimal(1.1)
