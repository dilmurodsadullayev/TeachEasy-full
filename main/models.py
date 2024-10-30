from django.db import models
import phonenumbers
from phonenumber_field.modelfields import PhoneNumberField


class UserRole(models.TextChoices):
    ADMIN = 'admin'
    TEACHER = 'teacher'
    STUDENT = 'student'

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=10, choices=UserRole.choices)


    def __str__(self):
        return self.username


class Owner(models.Model):
    full_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    address = models.CharField(max_length=60)
    image = models.ImageField(upload_to='owners/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name


class Teacher(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    image = models.ImageField(upload_to='teachers/')
    address = models.CharField(max_length=60)
    personal_phone = PhoneNumberField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name

class Student(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    image = models.ImageField(upload_to='students/')
    address = models.CharField(max_length=60)
    personal_phone = PhoneNumberField(blank=True)
    parent_phone = PhoneNumberField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name




class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')
    which_date = models.DateField()
    which_end_date = models.DateField()
    which_days = models.CharField(max_length=70)

    def __str__(self):
        return self.name




class CourseStudent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    start_date = models.DateField()

    def __str__(self):
        return f"{self.course.name} - {self.student}"



class Attendance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()


    def __str__(self):
        return f"{self.course.name} - {self.date}"


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    is_attendent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {str(self.is_attendent)}"


class CourseTask(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.course.name} - {self.name}"


class StudentTask(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_done = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.course.name} - {self.name} {self.is_done}"


class Payment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    price = models.FloatField()
    pay_date = models.DateField()
    payment_method = models.CharField(max_length=20)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course.name} - {self.student} {str(self.is_paid)}"


