from django.http import Http404
from django_filters import rest_framework as filters
# Create your views here.
# ViewSets define the view behavior.
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Faculty, Class, Schedule, Responsibility
from app.serializers import FacultySerializer, ClassSerializer, ScheduleSerializer, ResponsibilitySerializer


class FacultyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    filter_backends = (SearchFilter, filters.DjangoFilterBackend)
    filter_fields = ('faculty_id', 'password', 'name', 'dept', 'incharge_of', 'faculty_type', 'email')
    search_fields = ('faculty_id', 'name')

class ClassViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('class_id', 'year', 'dept', 'section', 'location')


class ScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filter_fields = ('class_id', 'faculty_id', 'subj_code', 'day', 'hour')
    ordering_fields = ('day', 'hour')
    ordering = ('day', 'hour')


class ResponsibilityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Responsibility.objects.all()
    serializer_class = ResponsibilitySerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filter_fields = ('responsibility_name',)
    search_fields = ('responsibility_name',)


class AuthViewSet(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, faculty_id, password):
        try:
            return Faculty.objects.get(faculty_id=faculty_id, password=password)
        except Faculty.DoesNotExist:
            raise Http404

    def get(self, request):
        faculty_id = self.request.query_params.get('faculty_id', None)
        password = self.request.query_params.get('password', None)
        faculty = self.get_object(faculty_id, password)
        serializer = FacultySerializer(faculty, context={'request': request})
        return Response(serializer.data)


class AvailabiltyViewSet(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, dept, day, hour):
        try:
            set1 = Faculty.objects.filter(dept=dept, faculty_schedule__day=day, faculty_schedule__hour=hour).values(
                'faculty_id')
            set2 = Faculty.objects.filter(dept=dept).exclude(faculty_id__in=set1).values('faculty_id', 'name', 'phone',
                                                                                         'faculty_type', 'email',
                                                                                         'dept', 'incharge_of')
            return set2
        except Faculty.DoesNotExist:
            raise Http404

    def get(self, request):
        dept = self.request.query_params.get('dept', None)
        day = self.request.query_params.get('day', None)
        hour = self.request.query_params.get('hour', None)
        availability = self.get_object(dept, day, hour)
        return Response(availability)
