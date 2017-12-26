from rest_framework import serializers

from app.models import Faculty, Class, Schedule, Responsibility


class FacultySerializer(serializers.ModelSerializer):
    faculty_schedule = serializers.SerializerMethodField()

    class Meta:
        model = Faculty
        fields = (
            'faculty_id', 'dept', 'name', 'email', 'password', 'phone', 'faculty_type', 'incharge_of',
            'faculty_schedule')

    def get_faculty_schedule(self, obj):
            return Schedule.objects.filter(faculty_id=obj.faculty_id).values('class_id', 'subj_code', 'day', 'hour',
                                                                             'class_id__location')


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('faculty_id', 'class_id', 'subj_code', 'day', 'hour')


class ClassSerializer(serializers.ModelSerializer):
    class_timetable = serializers.SerializerMethodField()

    class Meta:
        model = Class
        fields = ('class_id', 'dept', 'year', 'section', 'location', 'class_timetable')

    def get_class_timetable(self, obj):
        return Schedule.objects.filter(class_id=obj.class_id).values('faculty_id__name', 'subj_code', 'day', 'hour')


class ResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsibility
        fields = '__all__'
