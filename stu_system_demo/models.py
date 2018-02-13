from django.db import models


# Create your models here.

# 教师表
class Teachers(models.Model):
    t_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    age = models.IntegerField(max_length=5)
    sex = models.IntegerField(max_length=1)


# 课程表
class Course(models.Model):
    c_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    teacher = models.ForeignKey('Teachers', to_field='t_id', on_delete=models.CASCADE)


# 班级表
class StuClass(models.Model):
    name = models.CharField(max_length=32)
    course = models.ForeignKey('Course', to_field='c_id', on_delete=models.CASCADE)


# 学生表
class Students(models.Model):
    s_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    sex = models.IntegerField(max_length=1)
    age = models.IntegerField(max_length=5)
    stu_class = models.ForeignKey("StuClass", to_field='id', on_delete=models.CASCADE)
