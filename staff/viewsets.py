from rest_framework import viewsets, permissions
from staff.serializers import *


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by('id')
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset
