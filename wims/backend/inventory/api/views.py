# inventory/api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from inventory.models import Item  # Adjust based on your model
from inventory.api.serializers import ItemSerializer  # Ensure you have an ItemSerializer
from rest_framework import viewsets


class ItemListCreateAPIView(APIView):
    """
    List all items, or create a new item.
    """

    def get(self, request, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# Add more views as needed for other operations
