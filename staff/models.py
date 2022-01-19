from django.db import models
from django.contrib.auth.models import User


class Staff(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    mobile_no = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, default=None)
