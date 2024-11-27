from django.shortcuts import get_object_or_404, redirect,render
from .models import Course,UserSay,CustomUser,Student,Teacher
from .forms import CourseCreateForm,UserSayForm,CustomUserCreationForm
from django.views.generic import View
from django.contrib.auth import get_user_model,authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here

class IndexView(View):
    @method_decorator(login_required)
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
    

    ctx = {
    
    }
    return render(request, 'main/about.html',ctx)


def contact_view(request):
    return render(request, 'main/contact.html')


#Course

class CoursesView(View):
    template_name = 'course/courses.html'

    def get(self, request):
        # if not request.user.is_authenticated:
        #     messages.error(request, "Tizimga kirishingiz kerak.")
        #     return redirect('login')
        if request.user.is_authenticated:

            if request.user.role == "ADMIN" or request.user.role == "STUDENT":
                # ADMIN uchun barcha kurslar
                course_data = Course.objects.all()
                form = CourseCreateForm()
                ctx = {
                    'course_data': course_data,
                    'form': form,
                }
                return render(request, self.template_name, ctx)
            
            elif request.user.role == "TEACHER":
                # O'qituvchi faqat o'z kurslarini ko'radi
                
                teacher_id = Teacher.objects.get(user=request.user.id)
                print(teacher_id)
                course_data = Course.objects.filter(teacher=teacher_id)
                form = CourseCreateForm()
                ctx = {
                    'course_data': course_data,
                    'form': form,
                }
                return render(request, self.template_name, ctx)
            
            else:
                # Boshqa foydalanuvchilar uchun bu sahifani ko'rsatmaslik
                messages.error(request, "Sizda kurslar ro'yxatini ko'rish yoki yaratish huquqi yo'q.")
                return redirect('index')  # Yoki boshqa sahifaga yo'naltirish
        else:
            course_data = Course.objects.all()
            form = CourseCreateForm()
            ctx = {
                'course_data': course_data,
                'form': form,
            }
            return render(request, self.template_name, ctx)
            
    def post(self, request):
        # Foydalanuvchi tizimga kirganmi?
        if not request.user.is_authenticated:
            messages.error(request, "Kurs yaratish uchun tizimga kirishingiz kerak.")
            return redirect('login')

        form = CourseCreateForm(request.POST, request.FILES)

        if form.is_valid():
            course = form.save(commit=False)

            # Faqat Admin yoki O'qituvchi kurs yaratishi mumkin
            if request.user.role == "TEACHER":
                teacher, created = Teacher.objects.get_or_create(user=request.user)
                course.teacher = teacher
            else:
                messages.error(request, 'Faqat Admin yoki O\'qituvchi kurs yaratishi mumkin.')
                return redirect('courses')

            course.save()
            messages.success(request, 'Kurs muvaffaqiyatli yaratildi!')
            return redirect('courses')
        else:
            messages.error(request, 'Formada xatoliklar mavjud.')
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

        # Agar form noto'g'ri bo'lsa, kurslarni qayta yuklab va formni ko'rsatamiz
        course_data = Course.objects.all()
        ctx = {
            'form': form,
            'course_data': course_data,
        }
        return render(request, self.template_name, ctx)

def course_update_view(request,course_id):
    course = Course.objects.get(pk=course_id)

    ctx = {
        'course': course
    }

    return render(request, 'course/course_edit.html', ctx)

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
    return render(request, 'course/course_students.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'STUDENT'  # Default rolni belgilash
            user.save()

            # filter yordamida faqat bitta studentni olish
            student = Student.objects.filter(user=user).first()  # Birinchi studentni olish

            if not student:
                # Agar student mavjud bo'lmasa, yangi yaratamiz
                Student.objects.create(user=user)

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
    


def error_404_view(request):
    return render(request,'main/404.html'
    )




def change_user_role(request, user_id, new_role):
    user = get_object_or_404(CustomUser, id=user_id)
    user.role = new_role
    user.save()  # Signal avtomatik ravishda ishlaydi
    return redirect('user_list') 