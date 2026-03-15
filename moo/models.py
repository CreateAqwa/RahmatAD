from django.db import models

# from distutils.command.upload import upload
from django.utils import timezone



class Student_Enroll_Model(models.Model):
    registrationno=models.CharField(max_length=30 ,default="")
    name=models.CharField(max_length=30 ,default="")
    fathername=models.CharField(max_length=30 ,default="")
    mothername=models.CharField(max_length=30 ,default="")
    mobno=models.CharField(max_length=30 ,default="")
    city=models.CharField(max_length=30 ,default="")
    message=models.CharField(max_length=30 ,default="")
    gender=models.CharField(max_length=30 ,default="")
    course=models.CharField(max_length=30 ,default="")
    batchtime=models.CharField(max_length=30 ,default="")
    Photo=models.ImageField(upload_to="static/StudentEnroll", default="studentimage/default.jpg" ,blank=True,null=True)
    fee=models.CharField(max_length=30 ,default="")
    paidfee = models.IntegerField(default=0)
    remaningfee=models.CharField(max_length=50 ,default="")
    DateNow=models.DateTimeField(default=timezone.now)
    Date_Admission=models.CharField(default='none',max_length=200)


    def __str__(self):
        print(self.DateNow,'-----models Side')    
        return self.name


class aa(models.Model):
    registrationno=models.CharField(max_length=30 ,default="")
    name=models.CharField(max_length=30 ,default="")
    fathername=models.CharField(max_length=30 ,default="")
    mothername=models.CharField(max_length=30 ,default="")
    mobno=models.CharField(max_length=30 ,default="")
    city=models.CharField(max_length=30 ,default="")
    message=models.CharField(max_length=30 ,default="")
    gender=models.CharField(max_length=30 ,default="")
    course=models.CharField(max_length=30 ,default="")
    batchtime=models.CharField(max_length=30 ,default="")
    Photo=models.ImageField(upload_to="static/studentimage",default="")
    fee = models.IntegerField(default=0)
    paidfee = models.IntegerField(default=0)
    remaningfee = models.IntegerField(default=0)
    DateNow=models.DateTimeField(default=timezone.now)
    Date_Admission=models.CharField(default='none',max_length=200)
    FEES_DATE = models.DateField(null=True, blank=True)
    NEXT_FEES_DATE = models.DateField(null=True, blank=True)

    
    def __str__(self):
        print(self.DateNow,'-----models Side')    
        return self.name

class FeesHistory(models.Model):

    student = models.ForeignKey(aa, on_delete=models.CASCADE)

    FEES_DATE = models.DateField()

    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.student.name
        
           
class bb(models.Model):
    registrationno=models.CharField(max_length=30 ,default="")
    name=models.CharField(max_length=30 ,default="")
    fathername=models.CharField(max_length=30 ,default="")
    mothername=models.CharField(max_length=30 ,default="")
    mobno=models.CharField(max_length=30 ,default="")
    city=models.CharField(max_length=30 ,default="")
    message=models.CharField(max_length=30 ,default="")
    gender=models.CharField(max_length=30 ,default="")
    course=models.CharField(max_length=30 ,default="")
    batchtime=models.CharField(max_length=30 ,default="")
    Photo=models.ImageField(upload_to="static/studentimage",default="")
    fee = models.IntegerField(default=0)
    paidfee = models.IntegerField(default=0)
    remaningfee = models.IntegerField(default=0)
    DateNow=models.DateTimeField(default=timezone.now)
    Date_Admission=models.CharField(default='none',max_length=200)

    
    def __str__(self):
        return self.name
