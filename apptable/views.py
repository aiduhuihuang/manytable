from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
#测试页面
def index(request):

    return  HttpResponse("测试页面")

#数据的增加
def add(request):
    #create 增加并创建关系
    #正向
    #新老师 老王 教 新同学 小白
    #添加新老师 create返回这个数据对象
    # t_obj=Teacher.objects.create(name="老王",age=40,gender=1)
    # print(t_obj)
    # #利用正向添加了新的同学
    # p_obj=t_obj.person.create(name="小白",age=24)
    # print(p_obj)

    #反向
    # p_obj=Person.objects.create(name="小李",age=20)
    # p_obj.teacher_set.create(name="老李",age=50,gender=0)

    #add 对已存在数据增加关系
    #正向
    t_obj=Teacher.objects.filter(name="老李").first()
    print(t_obj)
    p_obj=Person.objects.filter(name="小白").first()
    print(p_obj)

    s=t_obj.person.add(p_obj)
    print(s)


    return HttpResponse("多对多的数据增加")

#查询
def gets(request):
    #正向
    #老李教过的学生
    # t_obj=Teacher.objects.filter(name="老李").first()
    # p_obj=t_obj.person.all().filter(name="小白")
    # print(p_obj)

    #反向
    #教学生小白的老师
    p_obj=Person.objects.filter(name="于雪").first()
    t_obj=p_obj.teacher_set.all().values()
    print(t_obj)

    return HttpResponse("多对多的数据查询")

#修改
def update(request):
    #正向
    # 老王 讲id为3的改成5 老王
    # t_obj=Teacher.objects.filter(name="老李").first()
    # p_obj=Person.objects.filter(name="于雪").first()
    # #内是一个列表
    # p_obj=t_obj.person.set([p_obj])
    # print(p_obj)

    #反向
    p_obj=Person.objects.filter(name="王大").first()
    # t_obj=Teacher.objects.filter(name="张宇").first()
    p_obj.teacher_set.set([1,6])

    return HttpResponse("多对多的数据修改")

#删除
def delete(request):
    #remove 解除指定数据间的关系
    #正向

    #反向

    #clear
    #正向 消除teacher_id为1的数据关系
    # t_obj=Teacher.objects.get(id=1)
    # s=t_obj.person.clear()
    # print(s)

    #delete
    # 删除person_id=1的数据
    p_obj=Person.objects.filter(id=1).delete()
    print(p_obj)
    return HttpResponse("多对多的数据删除")

#导入包
from django.db.models import *
def torm(request):
    data=Person.objects.values().aggregate(maxage=Max("age"),avgage=Avg("age"))
    print(data)
    return  HttpResponse("聚合函数和F/Q")