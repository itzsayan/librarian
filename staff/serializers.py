from rest_framework import serializers
from django.contrib.auth.models import User
from staff.models import *
from student.models import *
from datetime import datetime


class StaffSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50, allow_null=False, allow_blank=False)
    password = serializers.CharField(max_length=100, allow_blank=False, allow_null=False, write_only=True)
    first_name = serializers.CharField(max_length=150, allow_blank=False, allow_null=False)
    last_name = serializers.CharField(max_length=150, allow_null=False, allow_blank=False)
    email = serializers.CharField(max_length=50, allow_blank=False, allow_null=False)
    mobile_no = serializers.IntegerField(allow_null=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Staff
        fields = ["id", "mobile_no", "created_at", "updated_at", "email", "first_name", "last_name", "username", "password"]

    def create(self, validated_data):
        print(validated_data)
        mobile_no = validated_data["mobile_no"]
        email = validated_data["email"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        password = validated_data["password"]
        username = validated_data["username"]
        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return Staff.objects.create(user=user, mobile_no=mobile_no)

    def update(self, instance, validated_data):
        mobile_no = validated_data["mobile_no"]
        instance.mobile_no = mobile_no
        instance.save()
        return instance

    def to_representation(self, instance):
        # data = super(StaffSerializer, self).to_representation(instance)
        data = {
            "mobile_no": instance.mobile_no,
            "first_name": instance.user.first_name,
            "last_name": instance.user.last_name,
            "email": instance.user.email,
            "username": instance.user.username,
        }
        # data.update({
        #
        # })
        return data
