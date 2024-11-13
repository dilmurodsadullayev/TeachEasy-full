from django.shortcuts import render
from .models import UserRoles

# Create your views here.
def index_view(request):
    return render(request, 'main/index.html')



def about_view(request):
    user_roles = UserRoles.objects.all()

    ctx = {
        'user_roles': user_roles
    }
    return render(request, 'main/about.html',ctx)


def contact_view(request):
    return render(request, 'main/contact.html')

def courses_view(request):
    return render(request, 'main/courses.html')

def teachers_view(request):
    return render(request, 'main/teachers.html')


def gallery_view(request):
    return render(request, 'main/gallery.html')

def single_view(request):
    return render(request, 'main/single.html')

def blogs_view(request):
    return render(request, 'main/blog.html')

def course_students_view(request):
    return render(request, 'main/course_students.html')


def signup_view(request):
    return render(request, 'registration/sign_up.html')

def sign_in_view(request):
    return render(request, 'registration/sign_in.html')

def student_detail_view(request):
    return render(request, 'main/student_detail.html')


def group_tasks_view(request):
    return render(request, 'main/group_tasks.html')

# attendance
def attendances_view(request):
    return render(request, 'attendances/attendances.html')


def attendance_take_view(request):
    return render(request, 'attendances/attendance_take.html')

def attendance_update_view(request):
    return render(request, 'attendances/attendance_update.html')

def create_group_task_view(request):
    return render(request,'main/create_group_task.html')

#Teacher
def teacher_detail_view(request):
    return render(request,'main/teacher_detail.html')

def teacher_edit_view(request):
    return render(request,'main/teacher_edit.html')


def profile_view(request):
    return render(request, 'main/profile.html')
    

