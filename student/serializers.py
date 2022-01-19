from rest_framework import serializers
from django.contrib.auth.models import User
from student.models import *
from staff.models import *
from datetime import datetime


class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50, allow_null=False)
    password = serializers.CharField(max_length=100, allow_null=False, write_only=True)
    first_name = serializers.CharField(max_length=150, allow_null=False)
    last_name = serializers.CharField(max_length=150, allow_null=False)
    email = serializers.CharField(max_length=50, allow_null=False)
    gender = serializers.CharField(max_length=30)
    mobile_no = serializers.IntegerField()
    batch_year = serializers.IntegerField()
    stream = serializers.CharField(max_length=30)
    semester = serializers.CharField(max_length=30)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Student
        fields = ["id", "username", "password", "first_name", "last_name", "email", "gender", "mobile_no", "created_at",
                  "updated_at", "batch_year", "stream", "semester"]

    def create(self, validated_data):
        print(validated_data)
        username = validated_data["username"]
        password = validated_data["password"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        email = validated_data["email"]
        gender = validated_data["gender"]
        mobile_no = validated_data["mobile_no"]
        batch_year = validated_data["batch_year"]
        stream = validated_data["stream"]
        semester = validated_data["semester"]
        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return Student.objects.create(user=user, gender=gender, mobile_no=mobile_no, batch_year=batch_year,
                                      stream=stream, semester=semester)

    def update(self, instance, validated_data):
        mobile_no = validated_data["mobile_no"]
        stream = validated_data["stream"]
        semester = validated_data["semester"]
        instance.mobile_no = mobile_no
        instance.stream = stream
        instance.semester = semester
        instance.save()
        return instance

    def to_representation(self, instance):
        data = {
            "mobile_no": instance.mobile_no,
            "gender": instance.gender,
            "first_name": instance.user.first_name,
            "last_name": instance.user.last_name,
            "email": instance.user.email,
            "username": instance.user.username,
            "batch_year": instance.batch_year,
            "stream": instance.stream,
            "semester": instance.semester,
        }
        return data


class StudentBookRequisitionSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(allow_null=False)
    staff_id = serializers.IntegerField(allow_null=False)
    book_id = serializers.IntegerField(allow_null=False)
    is_submitted = serializers.BooleanField(default=False, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = StudentBookRequisition
        fields = ["id", "student_id", "staff_id", "book_id", "is_submitted", "created_at", "updated_at"]

    def update(self, instance, validated_data):
        instance.is_submitted = True
        instance.updated_at = datetime.now()
        instance.save()
        return instance
