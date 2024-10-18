from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Item
from .serializers import ItemSerializer

class InventoryViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self,request,*args):
        """ Use to create/Insert the New items in the sports inventory
        Args:
            request (json data): input to create inventory

        Returns:
            Json: It will return the output in json format success/failure
        """
        item_data = request.data
        serializer = ItemSerializer(data=item_data)
        if serializer.is_valid():
            try:
                item_data_creation = Item.objects.create(name = item_data.get("name"),description=item_data.get("description"),
                                        quantity=item_data.get("quantity"))
                item_data_creation.save()
            except:
                return Response({"error":"Item has not inserted"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"success":"Item has inserted in inventory"}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """ To update the item data if any needs to changes 

        Args:
            request (json): ID will be provided through query paramter

        Returns:
            Json: Returns Success/Failure response
        """
        
        super().update(request, *args, **kwargs)

        return Response({"success":"Item has updated Successfully"}, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        """ To get a list of items available in inventory

        Returns:
            Json: It will return list of items available in the inventory
        """
        if request.query_params.get('unavailable') == 'true':
            items = Item.objects.filter(quantity=0)
            # import pdb;pdb.set_trace()
            return Response({"items":[i.name for i in items]})
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """ It will provide the data for the given id 

        Args:
            request (json): Id as query parameter to retrieve data

        Returns:
            json: it will return the particular item
        """
        return super().retrieve(request, *args, **kwargs)
