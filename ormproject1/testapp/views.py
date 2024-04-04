from django.shortcuts import render
from .models import EmployeeModel
# from django.
# Create your views here.
from django.db.models import Q
def display(request):
    # details=EmployeeModel.objects.all()
    # details=EmployeeModel.objects.filter(id=1)
    # details=EmployeeModel.objects.filter(id__exact=1)
    # details=EmployeeModel.objects.filter(ename__contains='a')
    # details=EmployeeModel.objects.filter(id__in=[1,1000,1,2,3,4,5])
    # details=EmployeeModel.objects.filter(esal__gt=40000)
    # details=EmployeeModel.objects.filter(esal__lte=12000)
    # details=EmployeeModel.objects.filter()
    # details=EmployeeModel.objects.filter(ename__startswith='s')
    # details=EmployeeModel.objects.filter(ename__endswith='s')
    # details=EmployeeModel.objects.filter(esal__range=[0,30000])
    # details=EmployeeModel.objects.filter(esal__gt=30000)|EmployeeModel.objects.filter(ename__startswith='s')
    # details=EmployeeModel.objects.filter(Q(ename__startswith='z')|Q(esal__lt=25000))
    # details=EmployeeModel.objects.filter(ename__startswith='s') & EmployeeModel.objects.filter(esal__exact=39952.0)
    # details=EmployeeModel.objects.filter(Q(ename__startswith='a') &  Q(esal__gt=30000))
    # details=EmployeeModel.objects.filter(ename__startswith='a',ename__endswith='t')
    # print(len(details))
    # print(details)
    # details=EmployeeModel.objects.exclude(ename__startswith='s')
    # details=EmployeeModel.objects.filter(~Q(ename__startswith='j'))
    # details=EmployeeModel.objects.all().values_list('ename','esal')
    # details=EmployeeModel.objects.all().value('ename','esal')
    details=EmployeeModel.objects.all().only('ename','esal')
    from django.db.models import Avg,Min,Max,Sum,Count
    hi=EmployeeModel.objects.all().aggregate(Avg('esal'))
    min=EmployeeModel.objects.all().aggregate(Min('esal'))
    max=EmployeeModel.objects.all().aggregate(Max('esal'))
    sum=EmployeeModel.objects.all().aggregate(Sum('esal'))
    count=EmployeeModel.objects.all().aggregate(Count('ename'))
    q1=EmployeeModel.objects.filter(esal__gt=15000)
    q2=EmployeeModel.objects.filter(esal__startswith='shiva')
    details=q1.union()
    return render(request,'testapp/display.html',{'details':details,'hii':hi['esal__avg']})

def specfic(request):
    from django.db.models.functions import Lower
    details=EmployeeModel.objects.all().values_list('ename','esal').order_by(Lower('ename'))
    return render(request,'testapp/specify.html',{'details':details})