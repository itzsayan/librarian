from rest_framework import viewsets, permissions
from inventory.serializers import *


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = [permissions.IsAuthenticated]
