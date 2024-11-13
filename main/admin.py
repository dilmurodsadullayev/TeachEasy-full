from django.contrib import admin
from .models import (
    UserRoles,
    User,
    Course,
    CourseStudent,
    Attendance,
    Mark,
    CourseTask,
    StudentTask,
    CoursePayment,
    TeacherPayment

)
# Register your models here.

admin.site.register(UserRoles)
admin.site.register(User)
admin.site.register(Course)
admin.site.register(CourseStudent)
admin.site.register(Attendance)
admin.site.register(Mark)
admin.site.register(CourseTask)
admin.site.register(StudentTask)
admin.site.register(CoursePayment)
admin.site.register(TeacherPayment)



