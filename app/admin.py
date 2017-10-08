from django.contrib import admin

# Register your models here.
from app.models import Faculty, Class, Schedule

admin.site.site_header = 'Black Board Administration'


class ClassInline(admin.TabularInline):
    verbose_name = "Class Incharge Of"
    model = Class


class ScheduleInline(admin.TabularInline):
    model = Schedule
    verbose_name = "Faculty Schedule"


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    search_fields = ['class_id']
    list_filter = ('dept', 'class_id')
    list_display = ('class_id', 'dept', 'location', 'section')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    search_fields = ['class_id', 'faculty_id']
    list_filter = ('subj_code', 'faculty_id', 'class_id')
    list_display = ('faculty_id', 'class_id', 'subj_code', 'day', 'hour')
    verbose_name = "Schedule Of Faculty"


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    inlines = [ScheduleInline]
    search_fields = ['name', 'faculty_id']
    list_filter = ('dept', 'faculty_type')
    list_display = ('faculty_id', 'dept', 'name', 'email', 'password', 'phone', 'faculty_type', 'incharge_of')
