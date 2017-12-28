from rest_framework import serializers

from app.models import Faculty, Class, Schedule, Responsibility


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = (
            'faculty_id', 'dept', 'name', 'email', 'phone', 'faculty_type', 'incharge_of')

class ScheduleSerializer(serializers.ModelSerializer):
    class_location = serializers.SerializerMethodField()
    subj_name = serializers.SerializerMethodField()
    faculty_name = serializers.SerializerMethodField()
    class Meta:
        model = Schedule
        fields = ('faculty_name', 'class_id', 'class_location', 'subj_code', 'subj_name', 'day', 'hour')

    def get_class_location(self, obj):
        return obj.class_id.location.block_name.block_name + '-' + obj.class_id.location.room_name

    def get_subj_name(self, obj):
        return obj.subj_code.subject_name

    def get_faculty_name(self, obj):
        return obj.faculty_id.name

class ClassSerializer(serializers.ModelSerializer):
    class_timetable = serializers.SerializerMethodField()
    class_location = serializers.SerializerMethodField()
    class Meta:
        model = Class
        fields = ('class_id', 'dept', 'year', 'section', 'class_location', 'class_timetable')

    def get_class_timetable(self, obj):
        return ScheduleSerializer(Schedule.objects.filter(class_id=obj.class_id), many=True).data

    def get_class_location(self, obj):
        return obj.location.block_name.block_name + '-' + obj.location.room_name


class ResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsibility
        fields = '__all__'
