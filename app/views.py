from django.http import Http404
# Create your views here.
# ViewSets define the view behavior.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Faculty, Class, Schedule
from app.serializers import FacultySerializer, ClassSerializer, ScheduleSerializer


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


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
            set2 = Faculty.objects.filter(dept=dept).exclude(faculty_id__in=set1).values('faculty_id', 'name', 'phone')
            return set2
        except Faculty.DoesNotExist:
            raise Http404

    def get(self, request):
        dept = self.request.query_params.get('dept', None)
        day = self.request.query_params.get('day', None)
        hour = self.request.query_params.get('hour', None)
        availability = self.get_object(dept, day, hour)
        response = {}
        response['dept'] = dept
        response['day'] = day
        response['hour'] = hour
        response['availability'] = availability
        return Response(response)
