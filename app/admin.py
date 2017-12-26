from django.contrib import admin
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import Faculty, Class, Schedule, Responsibility

admin.site.site_header = 'Black Board Administration'


class FacultyResource(resources.ModelResource):
    class Meta:
        model = Faculty


class ScheduleResource(resources.ModelResource):
    class Meta:
        model = Schedule


class ClassResource(resources.ModelResource):
    class Meta:
        model = Class

class ClassInline(admin.TabularInline):
    verbose_name = "Class Incharge Of"
    model = Class


class ScheduleInline(admin.TabularInline):
    model = Schedule
    verbose_name = "Faculty Schedule"


@admin.register(Class)
class ClassAdmin(ImportExportModelAdmin):
    resource_class = ClassResource
    search_fields = ['class_id']
    list_filter = ('dept', 'class_id')
    list_display = ('class_id', 'dept', 'location', 'section')


@admin.register(Schedule)
class ScheduleAdmin(ImportExportModelAdmin):
    resource_class = ScheduleResource
    search_fields = ['class_id', 'faculty_id']
    list_filter = ('subj_code', 'faculty_id', 'class_id')
    list_display = ('faculty_id', 'class_id', 'subj_code', 'day', 'hour')
    verbose_name = "Schedule Of Faculty"


@admin.register(Faculty)
class FacultyAdmin(ImportExportModelAdmin):
    resource_class = FacultyResource
    inlines = [ScheduleInline]
    search_fields = ['name', 'faculty_id']
    list_filter = ('dept', 'faculty_type')
    list_display = ('faculty_id', 'dept', 'name', 'email', 'password', 'phone', 'faculty_type', 'incharge_of')


admin.site.register(Responsibility)
