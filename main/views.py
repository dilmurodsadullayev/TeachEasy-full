from django.shortcuts import render, redirect
from .models import UserRoles, AboutSite, Course
from .forms import CourseCreateForm
from django.views.generic import View


# Create your views here.
def index_view(request):
    return render(request, 'main/index.html')



def about_view(request):
    user_roles = UserRoles.objects.all()
    about_sites = AboutSite.objects.all()

    ctx = {
        'user_roles': user_roles,
        'about_sites': about_sites
    }
    return render(request, 'main/about.html',ctx)


def contact_view(request):
    return render(request, 'main/contact.html')


#Course
class CoursesView(View):
    def get(self, request):
        course_data = Course.objects.all()

        ctx = {
            'course_data': course_data
        }

        return render(request, 'course/courses.html', ctx)

    def post(self, request):
        form = CourseCreateForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.start_time = str(request.POST['start_time']) # Vaqt qiymatlarini str formatda olish
            course.end_time = str(request.POST['end_time'])#vaqti str formatda course.save()
            form.save()
            return redirect('courses')

        ctx = {
            'form': form
        }

        return render(request, 'course/courses.html', ctx)

def course_update_view(request):
    # course = Course.objects.get(pk=course_id)

    ctx = {
        # 'course': course
    }

    return render(request, 'course/course_update.html', ctx)

def course_delete_view(request):
    ctx = {

    }
    return render(request, 'course/course_delete.html', ctx)






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


def attendances_view(request):
    return render(request, 'attendances/attendances.html')

# attendance
def attendance_take_view(request):
    return render(request, 'attendances/attendance_take.html')


def attendance_update_view(request):
    return render(request, 'attendances/attendance_update.html')

def create_group_task_view(request):
    return render(request,'main/create_group_task.html')


#Teacher
def teacher_edit_view(request):
    return render(request,'teacher/teacher_edit.html')


def teachers_view(request):
    return render(request, 'teacher/teachers.html')


def teacher_detail_view(request):
    return render(request,'teacher/teacher_detail.html')


def profile_view(request):
    return render(request, 'main/profile.html')
    

