from rest_framework import viewsets, permissions
from student.serializers import *


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset


class StudentBookRequisitionViewSet(viewsets.ModelViewSet):
    queryset = StudentBookRequisition.objects.all()
    serializer_class = StudentBookRequisitionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        student_id = self.request.query_params.get('student_id')
        queryset = self.queryset.filter(student_id=student_id)
        is_submitted = self.request.query_params.get('is_submitted')
        if is_submitted is not None:
            queryset = self.queryset.filter(is_submitted=is_submitted)
        return queryset
