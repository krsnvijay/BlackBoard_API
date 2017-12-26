# Create your views here.
from rest_framework import viewsets

from choices_data.models import Block_Choices, Dept_Choices, Room_Choices, Subject_Choices, Faculty_Choices
from choices_data.serializers import BlockChoicesSerializer, DeptChoicesSerializer, RoomChoicesSerializer, \
    SubjectChoicesSerializer, FacultyChoicesSerializer


class BlockChoicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Block_Choices.objects.all()
    serializer_class = BlockChoicesSerializer


class DeptChoicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dept_Choices.objects.all()
    serializer_class = DeptChoicesSerializer


class RoomChoicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room_Choices.objects.all()
    serializer_class = RoomChoicesSerializer


class SubjectChoicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject_Choices.objects.all()
    serializer_class = SubjectChoicesSerializer


class FacultyChoicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Faculty_Choices.objects.all()
    serializer_class = FacultyChoicesSerializer
