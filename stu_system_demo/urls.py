
from django.conf.urls import url
from stu_system_demo import views

urlpatterns = [
    url('addstudent', views.addStudents, name='addstu'),
    url('checkstudents', views.checkStudentsList),
    url('index', views.index),
    url('checkTeachers', views.checkTeachersList),
    url('addteacher', views.addTeacher),
    url('addCourse', views.addCourse),
    url('checkCourseList', views.checkCourseList),
    url('addClass', views.addClass),
    url('checkClasssList', views.checkClasssList),
]