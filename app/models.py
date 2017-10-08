from django.db import models

# Create your models here.
from django.urls import reverse

CSE = 'CSE'
ECE = 'ECE'
IT = 'IT'
EEE = 'EEE'
CIVIL = 'CIVIL'
MECH = 'MECH'
DEPT_CHOICES = (
    (CSE, 'CSE'),
    (ECE, 'ECE'),
    (IT, 'IT'),
    (EEE, 'EEE'),
    (CIVIL, 'CIVIL'),
    (MECH, 'MECH'))
SECTION_CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('F', 'F'))
LOCATION_CHOICES = (
    ('ADMIN', (
        ('ADMIN-101', '101'),
        ('ADMIN-102', '102'),
        ('ADMIN-103', '103')
    )
     ),
    ('B.M.S', (
        ('B.M.S-101', '101'),
        ('B.M.S-102', '102'),
        ('B.M.S-103', '103')
    )
     ),
    ('BLOCK-III', (
        ('BLOCK-III-101', '101'),
        ('BLOCK-III-102', '102'),
        ('BLOCK-III-103', '103')
    )
     )
)


class Class(models.Model):
    class_id = models.CharField(max_length=30, primary_key=True, help_text='Enter Class ID eg.CSE-2-F', editable=False)
    location = models.CharField(max_length=30, help_text='Choose Class Location', choices=LOCATION_CHOICES)
    dept = models.CharField(max_length=5, choices=DEPT_CHOICES, help_text='Choose Department of the Class')
    year = models.CharField(max_length=1, choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')),
                            help_text='Choose Year Of The Class')
    section = models.CharField(max_length=1, help_text='Choose Section Of The Class', choices=SECTION_CHOICES)

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
        return reverse('model-detail-view', args=[str(self.class_id)])

    def save(self, *args, **kwargs):
        self.class_id = self.dept + "-" + self.year + "-" + self.section
        super(Class, self).save(*args, **kwargs)  # Call the "real" save()


class Faculty(models.Model):
    DEAN = 'DEAN'
    HOD = 'HOD'
    PROFESSOR = 'PROFESSOR'
    FACULTY_TYPE_CHOICES = (
        (DEAN, 'DEAN'),
        (HOD, 'HOD'),
        (PROFESSOR, 'PROFESSOR')
    )

    class Meta:
        verbose_name_plural = 'faculties'
        ordering = ["-faculty_id"]
    faculty_id = models.CharField(max_length=30, primary_key=True, help_text='Enter Faculty\'s College ID Number')
    name = models.CharField(max_length=30, help_text='Enter Faculty\'s Name')
    email = models.EmailField(max_length=50, help_text='Enter Faculty\'s Email')
    password = models.CharField(max_length=30, help_text='Enter Faculty\'s Password', default=123456)
    phone = models.CharField(max_length=10, help_text='Enter Faculty\'s Phone')
    dept = models.CharField(max_length=5, choices=DEPT_CHOICES, help_text='Choose Faculty\'s Dept')
    faculty_type = models.CharField(max_length=100, choices=FACULTY_TYPE_CHOICES,
                                    help_text='Choose Faculty\'s Designation')
    incharge_of = models.OneToOneField(Class, on_delete=models.CASCADE, null=True, related_name='of_class', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('model-detail-view', args=[str(self.faculty_id)])


class Schedule(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='faculty_schedule')
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='class_schedule')
    subj_code = models.CharField(max_length=10, help_text='Enter Subjcode')
    day = models.CharField(max_length=10, choices=(
        ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'),
        ('Friday', 'Friday')), help_text='Choose The Day')
    hour = models.CharField(max_length=1, help_text='Choose Section Of The Class', choices=(
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')))

    class Meta:
        verbose_name_plural = 'schedules'
        ordering = ["-faculty_id"]
        unique_together = ("class_id", "subj_code", "day", "hour")

    def __str__(self):
        return self.faculty_id_id
