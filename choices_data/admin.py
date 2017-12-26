from django.contrib import admin

# Register your models here.
from choices_data.models import Dept_Choices, Block_Choices, Room_Choices, Faculty_Choices, Subject_Choices


class RoomInline(admin.TabularInline):
    verbose_name = "Add Rooms"
    model = Room_Choices


@admin.register(Block_Choices)
class FacultyAdmin(admin.ModelAdmin):
    inlines = [RoomInline]


admin.site.register(Dept_Choices)
admin.site.register(Room_Choices)
admin.site.register(Faculty_Choices)
admin.site.register(Subject_Choices)
