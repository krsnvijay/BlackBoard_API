from django.core.validators import RegexValidator
from django.db import models
# Create your models here.
from django.urls import reverse

from choices_data.models import Dept_Choices, Room_Choices, Faculty_Choices, Subject_Choices

alpha_caps = RegexValidator(r'^[A-Z]', 'Only cap characters are allowed.')
year_validator = RegexValidator(r'^[1-5]', 'Only 1-5 are allowed.')
hour_validator = RegexValidator(r'^[1-7]', 'Only 1-7 are allowed.')


class Class(models.Model):
    class_id = models.CharField(max_length=30, primary_key=True, help_text='Enter Class ID eg.CSE-2-F', editable=False)
    location = models.ForeignKey(Room_Choices, on_delete=models.CASCADE, related_name='Room_choice')
    dept = models.ForeignKey(Dept_Choices, on_delete=models.CASCADE, related_name='Dept_choice')
    year = models.CharField(max_length=1, help_text='Enter year Of The Class', validators=[year_validator])
    section = models.CharField(max_length=1, help_text='Choose Section Of The Class', validators=[alpha_caps])

    class Meta:
        verbose_name_plural = 'classes'
        ordering = ["-class_id"]
        unique_together = ("class_id","location", "dept", "year", "section")

    def __str__(self):
        return self.class_id

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('class-detail', args=[str(self.class_id)])

    def save(self, *args, **kwargs):
        self.class_id = self.dept.dept_code + "-" + self.year + "-" + self.section
        super(Class, self).save(*args, **kwargs)  # Call the "real" save()


class Faculty(models.Model):

    class Meta:
        verbose_name_plural = 'faculties'
        ordering = ["-faculty_id"]
    faculty_id = models.CharField(max_length=30, primary_key=True, help_text='Enter Faculty\'s College ID Number')
    name = models.CharField(max_length=30, help_text='Enter Faculty\'s Name')
    email = models.EmailField(max_length=50, help_text='Enter Faculty\'s Email')
    password = models.CharField(max_length=30, help_text='Enter Faculty\'s Password', default=123456)
    phone = models.CharField(max_length=10, help_text='Enter Faculty\'s Phone')
    dept = models.ForeignKey(Dept_Choices, on_delete=models.CASCADE, related_name='dept_choice')
    faculty_type = models.ForeignKey(Faculty_Choices, on_delete=models.CASCADE, related_name='faculty_choice')
    incharge_of = models.OneToOneField(Class, on_delete=models.CASCADE, null=True, related_name='of_class', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('faculty-detail', args=[str(self.faculty_id)])


class Schedule(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='faculty_schedule')
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='class_schedule')
    subj_code = models.ForeignKey(Subject_Choices, on_delete=models.CASCADE, related_name='subject_choice')
    day = models.CharField(max_length=10, choices=(
        ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'),
        ('Friday', 'Friday')), help_text='Choose The Day')
    hour = models.CharField(max_length=1, help_text='Choose hour Of The Class', validators=[hour_validator])

    class Meta:
        verbose_name_plural = 'schedules'
        ordering = ["-faculty_id"]
        unique_together = ("class_id", "subj_code", "day", "hour")

    def __str__(self):
        return self.faculty_id_id

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('schedule-detail', args=[str(self.pk)])


class Responsibility(models.Model):
    responsibility_name = models.CharField(max_length=30, help_text='Enter Responsibility Name')
    faculties_responsible = models.ManyToManyField(Faculty)

    class Meta:
        verbose_name_plural = 'responsibilties'
        ordering = ["-responsibility_name"]

    def __str__(self):
        return self.responsibility_name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('responsibility-detail', args=[str(self.pk)])
