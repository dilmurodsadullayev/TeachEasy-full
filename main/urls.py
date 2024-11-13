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
    # registrations
    signup_view,
    sign_in_view,
#students
    student_detail_view,
    group_tasks_view,
    attendances_view,
    attendance_take_view,
    attendance_update_view,
    create_group_task_view,
#teachers
    teacher_detail_view,
    teacher_edit_view,

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
    path('sign-up',signup_view,name='signup'),
    path('sign-in',sign_in_view,name='signin'),
    #students
    path('student-detail',student_detail_view,name='student_detail'),
    path('group-tasks',group_tasks_view,name='group_tasks'),
    #attendance
    path('attendances',attendances_view,name='attendances'),
    path('attendance-take',attendance_take_view,name='attendance_take'),
    path('attendance-update',attendance_update_view,name='attendance_update'),
    path('create-group-task',create_group_task_view,name="create_group_task"),
    #teacher
    path('teacher-detail',teacher_detail_view,name="teacher_detail"),
    path('teacher-edit',teacher_edit_view,name='teacher_edit'),

]