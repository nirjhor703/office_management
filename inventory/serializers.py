from rest_framework import serializers
from .models import *

class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= ItemCategory
        fields='__all__'

class ItemFormSerializer(serializers.ModelSerializer):
    class Meta:
        model= ItemForm
        fields='__all__'
class ItemManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model= ItemManufacturer
        fields='__all__'
class ItemUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model= ItemUnit
        fields='__all__'     

        