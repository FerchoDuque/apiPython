from rest_framework import serializers
from bodega.models import Producto

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = (
            'codigo',
            'nombre',
            'estado',
            'fecha_ingreso'
        )
