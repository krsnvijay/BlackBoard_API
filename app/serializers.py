from rest_framework import serializers
from rest_framework.fields import DictField, CharField

from app.models import Faculty, Class, Schedule


class FacultySerializer(serializers.ModelSerializer):
    faculty_list = serializers.SerializerMethodField()  # add field
    faculty_schedule=serializers.SerializerMethodField()

    class Meta:
        model = Faculty
        fields = (
            'faculty_id', 'dept', 'name', 'email', 'password', 'phone', 'faculty_type', 'incharge_of','faculty_list','faculty_schedule')
    def get_faculty_list(self,obj):
        if(obj.faculty_type=="HOD"):
            return Faculty.objects.filter(dept=obj.dept).values('faculty_id', 'name')
        elif(obj.faculty_type=="DEAN"):
            return Faculty.objects.filter(faculty_type="HOD").values('faculty_id', 'name','phone','dept')
    def get_faculty_schedule(self,obj):
        if(obj.faculty_type=="PROFESSOR"):
            return Schedule.objects.filter(faculty_id=obj.faculty_id).values('class_id', 'subj_code', 'day', 'hour','class_id__location')
class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ('faculty_id', 'class_id', 'subj_code', 'day', 'hour')

class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class_timetable = serializers.SerializerMethodField()
    class Meta:
        model = Class
        fields = ('class_id', 'dept','year', 'section', 'location','class_timetable')
    def get_class_timetable(self,obj):
        return Schedule.objects.filter(class_id=obj.class_id).values('faculty_id__name', 'subj_code', 'day', 'hour')







class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('faculty_id','name','phone')
