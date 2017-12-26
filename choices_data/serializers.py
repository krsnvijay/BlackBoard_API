from rest_framework import serializers

from choices_data.models import Block_Choices, Dept_Choices, Room_Choices, Faculty_Choices, Subject_Choices


class BlockChoicesSerializer(serializers.ModelSerializer):
    rooms = serializers.SerializerMethodField()

    class Meta:
        model = Block_Choices
        fields = '__all__'

    def get_rooms(self, obj):
        return Room_Choices.objects.filter(block_name=obj.block_name).values('room_name')


class DeptChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dept_Choices
        fields = '__all__'


class RoomChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room_Choices
        fields = '__all__'


class FacultyChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty_Choices
        fields = '__all__'


class SubjectChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject_Choices
        fields = '__all__'
