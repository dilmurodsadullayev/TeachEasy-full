from django.shortcuts import render, redirect
from .models import AboutSite, Course,UserSay,CustomUser
from .forms import CourseCreateForm,UserSayForm,CustomUserCreationForm
from django.views.generic import View
from django.contrib.auth import get_user_model,authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here

class IndexView(LoginRequiredMixin,View):
    def post(self, request):
        form = UserSayForm(request.POST)
        if form.is_valid():
            user_say = form.save(user=request.user)  # Foydalanuvchini avtomatik qo'shish
            return redirect('index')
        else:
            ctx = {'form': form}
    
        return render(request, 'main/index.html', ctx)

    def get(self, request): 
        user_says = UserSay.objects.all()

        ctx = { 
            'user_says': user_says
        } 
        return render(request, 'main/index.html', ctx)

    



def about_view(request):
    about_sites = AboutSite.objects.all()

    ctx = {
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
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'STUDENT'  # Default rolni belgilash
            user.save()
            login(request, user)  # Foydalanuvchini tizimga kiritamiz
            return redirect('index')  # Bosh sahifaga yo'naltirish
        else:
            # Agar xatolik bo'lsa, u xatolikni foydalanuvchiga ko'rsatamiz
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'registrations/sign_up.html', {'form': form})




def sign_in_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Foydalanuvchini tizimga kiritamiz
                return redirect('index')  # Bosh sahifaga yo'naltirish
            else:
                messages.error(request, "Foydalanuvchi nomi yoki parol noto‘g‘ri")
        else:
            messages.error(request, "Foydalanuvchi nomi yoki parol noto‘g‘ri")
    else:
        form = AuthenticationForm()

    return render(request, 'registrations/sign_in.html', {'form': form})


def logout_view(request):
    logout(request)  # Foydalanuvchini tizimdan chiqarish
    return redirect('index')


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
    

