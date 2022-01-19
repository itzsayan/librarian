from rest_framework import serializers

from inventory.models import *


class BookSerializers(serializers.ModelSerializer):
    barcode = serializers.CharField(max_length=30)
    title = serializers.CharField(max_length=100, allow_blank=False, allow_null=False)
    author = serializers.CharField(max_length=50, allow_blank=False, allow_null=False)
    publisher = serializers.CharField(max_length=70, allow_blank=False, allow_null=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Book
        fields = ["id", "barcode", "title", "author", "publisher", "created_at", "updated_at"]
