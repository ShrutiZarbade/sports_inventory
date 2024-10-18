from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    """ Serializer for data validation part """
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'quantity']
