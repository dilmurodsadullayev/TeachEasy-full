from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'main/index.html')



def about_view(request):
    return render(request, 'main/about.html')


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
