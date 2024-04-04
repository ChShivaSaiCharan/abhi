import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ormproject1.settings')
import django
django.setup()
from testapp.models import EmployeeModel
# eno,ename,esal,eaddr
from faker import Faker
faker=Faker()
from random import *
def populate(n):
    for i in range(n):
        feno=randint(1,100)
        fename=faker.name()
        fesal=randint(10000,50000)
        faddr=faker.city()
        EmployeeModel.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=faddr)
    print('sucessfully created')

num=int(input('enter number'))
populate(num)