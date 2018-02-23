from django.shortcuts import render, HttpResponse, redirect
from stu_system_demo import models


# Create your views here.


# 首页
def index(request):
    return render(request, 'shool/index.html')


# 添加学生
def addStudents(request):
    if request.method == 'GET':
        obj = models.StuClass.objects.all()
        return render(request, 'shool/add_students.html', {'stu_class': obj})
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
    return render(request, 'shool/students_list.html', {'students_list': obj})


# 修改学生
def amendStudent(request):
    if request.method == 'GET':
        sid = request.GET.get('id')
        student = models.Students.objects.filter(s_id=sid).first()
        obj = models.StuClass.objects.all()
        return render(request, 'shool/amend_student.html', {"student": student, 'class': obj})
    elif request.method == 'POST':
        sid = request.POST.get('id')
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        class_id = request.POST.get('class')
        models.Students.objects.filter(s_id=sid).update(name=name, age=age, sex=sex, stu_class_id=class_id)
        return redirect('/demo1/checkstudents')


# 删除学生
def delStudent(request):
    sid = request.GET.get('id')
    models.Students.objects.filter(s_id=sid).delete()
    return redirect('/demo1/checkstudents')


# 查看教师列表
def checkTeachersList(request):
    obj = models.Teachers.objects.all()
    return render(request, 'shool/teacher_list.html', {'teachers_list': obj})


# 添加教师
def addTeacher(request):
    if request.method == 'GET':
        return render(request, 'shool/add_teacher.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        models.Teachers.objects.create(name=name, sex=sex, age=age)
        return redirect('/demo1/checkTeachers')


# 修改教师
def amendTeacher(request):
    if request.method == 'GET':
        tid = request.GET.get('id')
        teacher = models.Teachers.objects.filter(t_id=tid).first()
        return render(request, 'shool/amend_teacher.html', {"teacher": teacher})
    elif request.method == 'POST':
        tid = request.POST.get('id')
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        models.Teachers.objects.filter(t_id=tid).update(name=name, age=age, sex=sex)
        return redirect('/demo1/checkTeachers')


# 删除教师
def delTeacher(request):
    tid = request.GET.get('id')
    models.Teachers.objects.filter(t_id=tid).delete()
    return redirect('/demo1/checkTeachers')


# 添加课程
def addCourse(request):
    if request.method == 'GET':
        obj = models.Teachers.objects.all()
        return render(request, 'shool/add_course.html', {'teacher_list': obj})
    elif request.method == 'POST':
        name = request.POST.get('name')
        teacher_id = request.POST.get('teacher')
        models.Course.objects.create(name=name, teacher_id=teacher_id)
        return redirect('/demo1/checkCourseList')


# 课程列表
def checkCourseList(request):
    obj = models.Course.objects.all()
    return render(request, 'shool/course_list.html', {'course_list': obj})


# 编辑课程
def amendCourse(request):
    if request.method == 'GET':
        cid = request.GET.get('id')
        course = models.Course.objects.filter(c_id=cid).first()
        obj = models.Teachers.objects.all()
        return render(request, 'shool/amend_course.html', {'course': course, 'teacher': obj})
    elif request.method == 'POST':
        cid = request.POST.get('id')
        name = request.POST.get('name')
        teacher_id = request.POST.get('teacher')
        models.Course.objects.filter(c_id=cid).update(name=name, teacher_id=teacher_id)
        return redirect('/demo1/checkCourseList')


# 删除课程
def delCourse(request):
    cid = request.GET.get('id')
    models.Course.objects.filter(c_id=cid).delete()
    return redirect('/demo1/checkCourseList')


# 添加班级
def addClass(request):
    if request.method == 'GET':
        obj = models.Course.objects.all()
        return render(request, 'shool/add_class.html', {'course_list': obj})
    elif request.method == 'POST':
        name = request.POST.get('name')
        course_id = request.POST.get('course')
        models.StuClass.objects.create(name=name, course_id=course_id)
        return redirect('/demo1/checkClasssList')


# 班级列表
def checkClasssList(request):
    obj = models.StuClass.objects.all()
    return render(request, 'shool/class_list.html', {'class_list': obj})


# 编辑班级
def amendClass(request):
    if request.method == 'GET':
        cid = request.GET.get('id')
        stuClass = models.StuClass.objects.filter(id=cid).first()
        obj = models.Course.objects.all()
        return render(request, 'shool/amend_class.html', {'class': stuClass, 'course': obj})
    elif request.method == 'POST':
        cid = request.POST.get('id')
        name = request.POST.get('name')
        course_id = request.POST.get('course')
        models.StuClass.objects.filter(id=cid).update(name=name, course_id=course_id)
        return redirect('/demo1/checkClasssList')


# 删除班级
def delClass(request):
    cid = request.GET.get('id')
    models.StuClass.objects.filter(id=cid).delete()
    return redirect('/demo1/checkCourseList')
