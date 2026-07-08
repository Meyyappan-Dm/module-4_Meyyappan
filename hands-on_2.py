from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    head_of_dept = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    credits = models.IntegerField()
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    enrollment_year = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Enrollment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    enrollment_date = models.DateField()
    grade = models.CharField(
        max_length=2,
        null=True,
        blank=True
    )

    class Meta:
        unique_together = [['student', 'course']]

    def __str__(self):
        return f"{self.student} - {self.course}"



Course.objects.create(
    name="Python Programming",
    code="CS101",
    credits=4,
    department=cs
)

Course.objects.create(
    name="Database Systems",
    code="CS102",
    credits=3,
    department=cs
)

Course.objects.create(
    name="Operating Systems",
    code="CS103",
    credits=4,
    department=cs
)

Course.objects.create(
    name="Cloud Computing",
    code="IT201",
    credits=3,
    department=it
)


Student.objects.create(
    first_name="John",
    last_name="Doe",
    email="john@example.com",
    department=cs,
    enrollment_year=2023
)

Student.objects.create(
    first_name="Alice",
    last_name="Smith",
    email="alice@example.com",
    department=cs,
    enrollment_year=2022
)

Student.objects.create(
    first_name="Bob",
    last_name="Brown",
    email="bob@example.com",
    department=it,
    enrollment_year=2024
)

Student.objects.create(
    first_name="David",
    last_name="Lee",
    email="david@example.com",
    department=cs,
    enrollment_year=2023
)

Student.objects.create(
    first_name="Eva",
    last_name="Wilson",
    email="eva@example.com",
    department=it,
    enrollment_year=2024
)


