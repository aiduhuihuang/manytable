from django.db import models

# Create your models here.
#说明：一个学生可以有多个老师
#        一个老师也可以教多个学生
class Person(models.Model):
    name=models.CharField(max_length=20,verbose_name="学生姓名")
    age=models.IntegerField(verbose_name="学生年龄")
    #改元数据
    class Meta:
        db_table="person"
        verbose_name_plural="学生表"

class Teacher(models.Model):
    name=models.CharField(max_length=20,verbose_name="老师姓名")
    gender=models.IntegerField(verbose_name="性别") #1代表男,0代表女
    age=models.IntegerField(verbose_name="年龄")
    #建立多表关系，不需要建立第三张表(to 代表和哪个表产生关系)
    person=models.ManyToManyField(to=Person)

    class Meta:
        db_table="teacher"
        verbose_name_plural="老师表"