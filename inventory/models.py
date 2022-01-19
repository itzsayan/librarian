from django.db import models


class Book(models.Model):
    barcode = models.CharField(max_length=30)
    title = models.CharField(max_length=100, blank=False, null=False)
    author = models.CharField(max_length=50, blank=False, null=False)
    publisher = models.CharField(max_length=70, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, default=None)
