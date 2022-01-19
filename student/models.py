from django.db import models
from django.contrib.auth.models import User
from inventory.models import Book
from student.models import *
from staff.models import *


class Student(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=30, blank=False)
    mobile_no = models.IntegerField(blank=False)
    batch_year = models.IntegerField(blank=False, default=None)
    stream = models.CharField(max_length=30, blank=False, default=None)
    semester = models.CharField(max_length=30, blank=False, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, default=None)


class StudentBookRequisition(models.Model):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    staff = models.ForeignKey(to=Staff, on_delete=models.CASCADE)
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    is_submitted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, default=None)
