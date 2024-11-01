from django.conf.urls.i18n import urlpatterns
from django.urls import path
from .views import (
    index_view,
    about_view,
    contact_view,
    courses_view,
    teachers_view,
    gallery_view,
    single_view,
    blogs_view,
    course_students_view,
    #registrations
    signup_view,
    sign_in_view
)

urlpatterns = [
    path('',index_view,name='index'),
    path('about',about_view,name='about'),
    path('contact',contact_view,name='contact'),
    path('courses',courses_view,name='courses'),
    path('teachers',teachers_view,name='teachers'),
    path('gallery',gallery_view,name='gallery'),
    path('single',single_view,name='single'),
    path('blogs',blogs_view,name='blogs'),
    path('course-students',course_students_view,name='course_students'),
    # registration
    path('signup',signup_view,name='signup'),
    path('signin',sign_in_view,name='signin'),

]