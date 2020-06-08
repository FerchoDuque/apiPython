from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from bodega.models import Producto
from bodega.serializers import ProductoSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST','DELETE'])
def bodega_list(request):
    #GET Lista productos, POST un producto, DELETE todos los productos
    if request.method == 'GET':
        productos = Producto.objects.all()
        nombre = request.GET.get('nombre',None)
        if nombre is not None:
            productos = productos.filter(nombre__icontains=nombre)
        productos_serializer = ProductoSerializer(productos, many=True)
        return JsonResponse(productos_serializer.data, safe = False)
    elif request.method == 'POST':
        producto_data = JSONParser().parse(request)
        producto_serializer = ProductoSerializer(data=producto_data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return JsonResponse(producto_serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(producto_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Producto.objects.all().delete()
        return JsonResponse({'message':'{} Productos eliminados correctamente!'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST','PUT','DELETE'])
def bodega_detail(request, pk):
    #busca un producto por PK (id)
        try:
            producto = Producto.objects.get(codigo=pk)
            if request.method == 'GET':
                producto_serializer = ProductoSerializer(producto)
                return JsonResponse(producto_serializer.data)
            elif request.method == 'PUT':
                producto_data = JSONParser().parse(request)
                producto_serializer = ProductoSerializer(producto, data=producto_data)
                if(producto_serializer.is_valid()):
                    producto_serializer.save()
                    return JsonResponse(producto_serializer.data, safe = False)
                return JsonResponse(producto_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            elif request.method == 'DELETE':
                producto.delete()
                return JsonResponse({'message':'Producto Eliminado'}, status=status.HTTP_204_NO_CONTENT)
        except Producto.DoesNotExist:
            return JsonResponse({'message':'El producto no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def bodega_list_estado(request, estado):
    #obtiene todos los productos en estado entrada
    productos = Producto.objects.filter(estado=estado)
    if request.method == 'GET':
        productos_serialized = ProductoSerializer(productos, many=True)
        return JsonResponse(productos_serialized.data, safe=False)
