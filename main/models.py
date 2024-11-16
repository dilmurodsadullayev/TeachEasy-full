from django.db import models
import datetime
import phonenumbers
from django.db.models import URLField
from phonenumber_field.modelfields import PhoneNumberField


class AboutSite(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    creator_name = models.CharField(max_length=20)
    address = models.CharField(max_length=140)
    email = models.EmailField()
    phone = PhoneNumberField()
    instagram_url: URLField = models.URLField()
    telegram_url = models.URLField()
    instagram_url = models.URLField()
    github_url = models.URLField()
    linkedin_url = models.URLField()

    def __str__(self):
        return self.name


class UserRoles(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='role_images/')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name




class User(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True)
    email = models.EmailField(max_length=254, unique=True)  # Email uzunligini oshirdik
    password = models.CharField(max_length=128)  # Parol uzunligini oshirdik
    phone_number = PhoneNumberField(unique=True,blank=True, null=True)
    role = models.OneToOneField(UserRoles, on_delete=models.CASCADE,default=2)
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name






class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    start_time = models.TimeField()
    end_time = models.TimeField()  # tugash sanasi (oldingi
    schedule_days = models.CharField(max_length=70)  # o‘quv kunlari yoki `schedule` qisqacha

    def __str__(self):
        return self.name


class CourseStudent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_students')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_teachers')
    start_date = models.DateField()

    def __str__(self):
        return f"{self.course.name} - {self.student}"


class Attendance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{str(self.course.name)} - {self.date}"


class Mark(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='marks')
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    is_attended = models.BooleanField(default=False)  # is_attendent o'rniga is_attended

    def __str__(self):

        return f"{self.student} - {str(self.is_attended)}"




class CourseTask(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.course.name} - {self.name}"


class StudentTask(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_tasks')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course.name} - {self.name} {self.is_done}"


class CoursePayment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    price = models.FloatField()
    pay_date = models.DateField()
    payment_method = models.CharField(max_length=20)  # Bu yerga tanlov qo'shishingiz mumkin
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course.name} - {self.student} {self.is_paid}"



class TeacherPayment(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_payments')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='teacher_payments/')
    is_paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher.name} - {self.price}"



