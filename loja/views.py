from multiprocessing.dummy.connection import Client
from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cliente, Produto, Pedido
from .serializer import ProdutoSerializer, ClienteSerializer, PedidoSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def listar_produtos(request):
    if request.method == 'GET':
        queryset = Produto.objects.all()
        serializer = ProdutoSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])     
def produto_detalhe(request, id):
    produto = get_object_or_404(Produto, pk=id)

    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)     

        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProdutoSerializer(produto, data=request.data)    
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        produto.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def listar_clientes(request):
    if request.method == 'GET':
        queryset = Cliente.objects.all()
        serializer = ClienteSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def cliente_detalhe(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ClienteSerializer(Cliente, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

@api_view(['GET', 'POST'])
def listar_pedidos(request):
    if request.method == 'GET':
        queryset = Pedido.objects.all()
        serializer = PedidoSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PedidoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pedido_detalhe(request, id):
    pedido = get_object_or_404(Pedido, pk=id)

    if request.method == 'GET':
        serializer = PedidoSerializer(Pedido)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PedidoSerialzier(Pedido, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

