from django.contrib import admin
from .models import (
    CustomUser,
    Course,
    CourseStudent,
    Attendance,
    Mark,
    CourseTask,
    StudentTask,
    CoursePayment,
    TeacherPayment,
    AboutSite,
    UserSay

)
# Register your models here.
class UserSayAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_time') 

admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(CourseStudent)
admin.site.register(Attendance)
admin.site.register(Mark)
admin.site.register(CourseTask)
admin.site.register(StudentTask)
admin.site.register(CoursePayment)
admin.site.register(TeacherPayment)
admin.site.register(AboutSite)
admin.site.register(UserSay,UserSayAdmin)



