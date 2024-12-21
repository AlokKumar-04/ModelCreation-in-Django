from django.db import models

# Create your models here.
class Country(models.Model):
    cname = models.CharField(max_length=200, primary_key=True)

class Capitals(models.Model):
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)
    capitala = models.CharField(max_length=100)

class Dept(models.Model):
    dname = models.CharField(max_length=50)
    loc = models.CharField(max_length=50)
    deptno = models.IntegerField

class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    hiredate = models.DateField
    sal = models.DecimalField(max_digits=5, decimal_places=2)
    comm = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank = True)
    deptno = models.ForeignKey(Dept, on_delete=models.CASCADE)
