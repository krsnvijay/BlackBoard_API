from django.db import models


# Create your models here.

class Dept_Choices(models.Model):
    dept_code = models.CharField(max_length=10, primary_key=True, help_text='Enter Dept (EEE,CSE..)')

    class Meta:
        verbose_name_plural = 'Department Choices'
        ordering = ["-dept_code"]

    def __str__(self):
        return self.dept_code


class Block_Choices(models.Model):
    block_name = models.CharField(max_length=30, primary_key=True, help_text='Enter Block Name (Admin,BMS..)')

    class Meta:
        verbose_name_plural = 'Block Choices'
        ordering = ["-block_name"]

    def __str__(self):
        return self.block_name


class Room_Choices(models.Model):
    block_name = models.ForeignKey(Block_Choices, on_delete=models.CASCADE, related_name='block_details')
    room_name = models.CharField(max_length=30, help_text='Enter room Name (101,201)')

    class Meta:
        verbose_name_plural = 'Room Choices'
        ordering = ["-room_name"]
        unique_together = ("block_name", "room_name")

    def __str__(self):
        return self.block_name.block_name + "-" + self.room_name


class Faculty_Choices(models.Model):
    faculty_type = models.CharField(max_length=30, primary_key=True,
                                    help_text='Enter Faculty Type (HOD,DEAN,Asst.Prof)')

    class Meta:
        verbose_name_plural = 'Faculty Choices'
        ordering = ["-faculty_type"]

    def __str__(self):
        return self.faculty_type


class Subject_Choices(models.Model):
    subject_code = models.CharField(max_length=30, primary_key=True, help_text='Enter Subject Code (15IT301)')
    subject_name = models.CharField(max_length=30, help_text='Enter Subject Name (Python)')

    class Meta:
        verbose_name_plural = 'Subject Choices'
        ordering = ["-subject_code"]

    def __str__(self):
        return self.subject_code + "-" + self.subject_name
