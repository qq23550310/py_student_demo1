from django.shortcuts import render, HttpResponse, redirect
from stu_system_demo import models


# Create your views here.


# 首页
def index(request):
    return render(request, 'index.html')


# 添加学生
def addStudents(request):
    if request.method == 'GET':
        obj = models.StuClass.objects.all()
        return render(request, 'add_students.html', {'stu_class': obj})
    elif request.method == 'POST':
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        stu_class_id = request.POST.get('class')
        models.Students.objects.create(name=name, sex=sex, age=age, stu_class_id=stu_class_id)
        return redirect('/demo1/checkstudents')


# 查看学生列表
def checkStudentsList(request):
    obj = models.Students.objects.all()
    return render(request, 'students_list.html', {'students_list': obj})


# 查看教师列表
def checkTeachersList(request):
    obj = models.Teachers.objects.all()
    return render(request, 'teacher_list.html', {'teachers_list': obj})


# 添加教师
def addTeacher(request):
    if request.method == 'GET':
        return render(request, 'add_teacher.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        models.Teachers.objects.create(name=name, sex=sex, age=age)
        return redirect('/demo1/checkTeachers')
