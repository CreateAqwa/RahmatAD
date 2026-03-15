
from moo.models import aa,bb,Student_Enroll_Model,FeesHistory
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

import os
from django.conf import settings


def home(request):
    from django.utils.timezone import now
    current_time = now()
    print(current_time)
    return render(request,"home.html")

def StudentEnroll(request):
    selectcolume={
        'cityy':["Delhi","Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa",
                 "Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka",
                 "Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland",
                 "Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura",
                 "Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands",
                 "Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","Puducherry"]
        }
    try:
        if request.method=="POST":
            registrationno="nan"
            fee='nan'
            remaningfee='nan'
            Date_Admission='nan'
            message='nan'
            name=request.POST.get("name")
            fathername=request.POST.get("fathername")
            mothername=request.POST.get("mothername")
            mobno=request.POST.get("mobno")
            city=request.POST.get("city")
            gender=request.POST.get("gender")
            course=request.POST.get("course")
            batchtime=request.POST.get("batchtime")
            Photo=request.FILES["Photo"]
            
            # print(Date_Admission,type(Date_Admission),'Date_Admission')
            
            # print('registrationno',registrationno,'name',name,'fathername',fathername,'mothername',mothername,
            #       'mobno',mobno,'city',city,'message',message,'gender',gender,'course',course,'batchtime',batchtime,'Photo',Photo,'fee',fee,'remaningfee',remaningfee,'Date_Admission',str(Date_Admission))

            mydata=Student_Enroll_Model(registrationno=registrationno,name=name,fathername=fathername,mothername=mothername,mobno=mobno,city=city,message=message,gender=gender,course=course,batchtime=batchtime,Photo=Photo,fee=fee,remaningfee=remaningfee,Date_Admission=str(Date_Admission))
            print(mydata.Date_Admission,'4 my daya')
            mydata.save()

            getalldataid=Student_Enroll_Model.objects.all().order_by("-id")[0]
            
            oldid=getalldataid.id
            registrationno="G-I_"+str(oldid)
            
            mydata=Student_Enroll_Model(id=oldid,registrationno=registrationno,name=name,fathername=fathername,mothername=mothername,mobno=mobno,city=city,message=message,gender=gender,course=course,batchtime=batchtime,Photo=Photo,fee=fee,remaningfee=remaningfee,Date_Admission=str(Date_Admission))
            mydata.save()
            print('DATA SAVED')
    except:
        pass
    return render(request,"StudentEnroll.html",selectcolume)



@login_required(login_url='/login/')
def View_Enroll_All(request):
    getalldataid=Student_Enroll_Model.objects.all().order_by("-id")
    
    getonebyone={
        "a":getalldataid
        }
    return render(request,"View_Enroll_All.html",getonebyone)






@login_required(login_url='/login/')
def registration(request):

    selectcolume={
        'cityy':["Delhi","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa",
                 "Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka",
                 "Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland",
                 "Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura",
                 "Uttar Pradesh","Uttarakhand","West Bengal"]}
    try:
        if request.method=="POST":

            registrationno="nan"
            name=request.POST.get("name")
            fathername=request.POST.get("fathername")
            mothername=request.POST.get("mothername")
            mobno=request.POST.get("mobno")
            city=request.POST.get("city")
            message=request.POST.get("message")
            gender=request.POST.get("gender")
            course=request.POST.get("course")
            batchtime=request.POST.get("batchtime")
            Photo=request.FILES["Photo"]

            fee=request.POST.get("fee")
            paidfee=request.POST.get("paidfee")

            Date_Admission=request.POST.get("Date_Admission")
            remaningfee=int(fee)-int(paidfee)
            # Student Save
            mydata=aa(
                registrationno=registrationno,
                name=name,
                fathername=fathername,
                mothername=mothername,
                mobno=mobno,
                city=city,
                message=message,
                gender=gender,
                course=course,
                batchtime=batchtime,
                Photo=Photo,
                fee=fee,
                paidfee=paidfee,
                remaningfee=remaningfee,
                Date_Admission=str(Date_Admission),
                NEXT_FEES_DATE = date.today() + timedelta(days=30)
            )
            
            mydata.save()

            # Registration Number Generate
            getalldataid=aa.objects.all().order_by("-id")[0]

            oldid=getalldataid.id
            registrationno="IT"+str(oldid)

            mydata.registrationno=registrationno
            mydata.save()


            # -------- Fees History Save --------

            FeesHistory.objects.create(

                student=mydata,
                FEES_DATE=date.today(),
                amount=fee

            )

    except:
        pass

    return render(request,"registration.html",selectcolume)

# ============VIEWW PAGE CONECTION START============================================




@login_required(login_url='/login/')
def vieww(request):
    return render(request,"vieww.html")






@login_required(login_url='/login/')
def viewalldata(request):
    students = aa.objects.all().order_by("-id")
    for s in students:
        last = FeesHistory.objects.filter(student=s).order_by("-id").first()
        if last:
            s.last_fee = last.FEES_DATE
        else:
            s.last_fee = "No Fee"
    return render(request,'viewalldata.html',{'all':students})

# def deletedata(request,uid):
#     get_id=aa.objects.get(id=uid)
#     get_id.delete()
#     url="/viewalldata/"
#     return HttpResponseRedirect(url)



from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
import os
from django.conf import settings

@login_required(login_url='/login/')
def deletedata(request, uid,Rpage):
    get_id = get_object_or_404(aa, id=uid)
    
    # print(get_id,'--delte')
    if get_id.Photo:
        photo_path = os.path.join(settings.MEDIA_ROOT, str(get_id.Photo))
        if os.path.exists(photo_path):
            os.remove(photo_path)
    get_id.delete()
    
    messages.success(request, "Student Record Deleted Successfully!")
    return redirect(Rpage)


@login_required(login_url='/login/')
def earchbatchtime(request):
    vars={
        "aaaaa":["10AM","11AM",'12AM',"1PM","2PM","3PM","4PM","5PM","6PM",'7PM','8PM','9PM']
    }
    try:
        if request.method=="POST":
            inputbatchtime=request.POST.get("inputbatchtime")
            url="/sendbatchtime/"+inputbatchtime
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"earchbatchtime.html",vars)


@login_required(login_url='/login/')
def sendbatchtime(request,inputbatchtime):
    print("BATCH TIME IS =>"+inputbatchtime)
    #  filter(inside model VAR name = inside html ya transfer data varibal name)
    abc=aa.objects.filter(batchtime=inputbatchtime)
    data={
        "aaaa":abc
    }
    return render(request,"sendbatchtime.html",data)


@login_required(login_url='/login/')
def searchregistration(request):
    try:
        if request.method=="POST":
            aqs=request.POST.get("registrationno")
            url="/registrationdata/"+aqs
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"searchregistration.html")


@login_required(login_url='/login/')
def registrationdata(request,aqs):
    aqsdata=aa.objects.filter(registrationno=aqs)
    sasa={
        "aaa":aqsdata
    }
    return render(request,"registrationdata.html",sasa)


@login_required(login_url='/login/')
def searchbyname(request):
    try:
        if request.method=="POST":
            byname=request.POST.get("byname")
            url="/bynamedata/"+byname
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"searchbyname.html")


@login_required(login_url='/login/')
def bynamedata(request,byname):
    viewname=aa.objects.filter(name=byname)
    dda={
        "as":viewname
    }
    return render(request,"bynamedata.html",dda)


# ============VIEWW PAGE CONNECTION END ============================================
@login_required(login_url='/login/')
def passoutentry(request):
    try:
        if request.method=="POST":
            deletedatabyreg=request.POST.get("deletedatabyreg")
            finded=aa.objects.get(registrationno=deletedatabyreg)
            
            registrationno=finded.registrationno
            name=finded.name
            fathername=finded.fathername
            mothername=finded.mothername
            mobno=finded.mobno
            city=finded.city
            message=finded.message
            gender=finded.gender
            course=finded.course
            batchtime=finded.batchtime
            Photo=finded.Photo
            fee=finded.fee
            remaningfee=finded.remaningfee
            sendtodelete=bb(registrationno=registrationno,name=name,fathername=fathername,mothername=mothername,mobno=mobno,city=city,
                            message=message,gender=gender,course=course,batchtime=batchtime,Photo=Photo,fee=fee,remaningfee=remaningfee,)
            sendtodelete.save()
            finded.delete()
    except:
        pass
    
    return render(request,"passoutentry.html")

@login_required(login_url='/login/')
def update(request):
    try:
        if request.method=="POST":
            regnodata=request.POST.get("regnodata")
            url="/updateuser/"+regnodata
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"update.html")

@login_required(login_url='/login/')
def updateuser(request,regnodata):
    fatchingUpdatedata=aa.objects.get(registrationno=regnodata)
    gotet={
        "data":fatchingUpdatedata
    }
    
    
    try:
        print(fatchingUpdatedata.DateNow,'aaaaaaa')
        print(fatchingUpdatedata.Photo,'pppp')

        if request.method=="POST":
            uid=fatchingUpdatedata.id
            rrrregnodata=fatchingUpdatedata.registrationno
            name=request.POST.get("name")
            fathername=request.POST.get("fathername")
            mothername=request.POST.get("mothername")
            mobno=request.POST.get("mobno")
            city=request.POST.get("city")
            message=request.POST.get("message")
            gender=request.POST.get("gender")
            course=request.POST.get("course")
            batchtime=request.POST.get("batchtime")
            # Photo=request.FILES["Photo"]
            Photo=request.POST.get("Photo")
            fee=request.POST.get("fee")
            remaningfee=request.POST.get("remaningfee")
            Date_Admission=request.POST.get("Date_Admission")
            print(Photo,'Photo')
            if Photo=='':
                print('1')
                mydata=aa(registrationno=rrrregnodata,id=uid,name=name,fathername=fathername,mothername=mothername,
                      mobno=mobno,city=city,message=message,gender=gender,course=course,batchtime=batchtime,Photo=fatchingUpdatedata.Photo,
                      fee=fee,remaningfee=remaningfee,Date_Admission=Date_Admission,DateNow=fatchingUpdatedata.DateNow)
                mydata.save()
                
            if Photo==None:
                print('2')
                Photo=request.FILES["Photo"]
                mydata=aa(registrationno=rrrregnodata,id=uid,name=name,fathername=fathername,mothername=mothername,
                      mobno=mobno,city=city,message=message,gender=gender,course=course,batchtime=batchtime,Photo=Photo,
                      fee=fee,remaningfee=remaningfee,Date_Admission=Date_Admission,DateNow=fatchingUpdatedata.DateNow)
                mydata.save()
                
            # mydata=aa(registrationno=rrrregnodata,id=uid,name=name,fathername=fathername,mothername=mothername,
            #           mobno=mobno,city=city,message=message,gender=gender,course=course,batchtime=batchtime,Photo=fatchingUpdatedata.Photo,
            #           fee=fee,remaningfee=remaningfee,Date_Admission=Date_Admission,DateNow=fatchingUpdatedata.DateNow)
            # mydata.save()
            # mydata=fatchingUpdatedata.delete("{{data.id}}")
            url="/viewalldata/"
            return HttpResponseRedirect(url)
    except:
        
        pass
    
    return render(request,"updateuser.html",gotet)


def feeshistory(request,id):
    student = aa.objects.get(id=id)
    history = FeesHistory.objects.filter(student=student)

    return render(request,"feeshistory.html",{
        "student":student,
        "history":history
    })




@login_required(login_url='/login/')
def fee(request):
    return render(request,"fee.html")


@login_required(login_url='/login/')
def submitfee(request):
    try:
        if request.method=="POST":
            regno=request.POST.get("regno")
            trn="/submitfee2/"+regno
            return HttpResponseRedirect(trn)
    except:
        pass
    return render(request,"submitfee.html")




from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

def submitfee2(request, regno):
    student = get_object_or_404(aa, registrationno=regno)
    if request.method == "POST":
        newfee = int(request.POST.get("newfee"))
        # 🔴 Check: fee remaining se zyada to alert
        if newfee > student.remaningfee:
            messages.error(
                request,
                f"Fee cannot be greater than remaining fee (₹{student.remaningfee})"
            )
            return redirect(f"/submitfee2/{regno}")
        # Paid fee update
        student.paidfee += newfee
        # Remaining calculate
        student.remaningfee = student.fee - student.paidfee


        student.FEES_DATE = date.today()


        student.NEXT_FEES_DATE = date.today() + timedelta(days=30)
        student.save()


        # Fee history save
        FeesHistory.objects.create(
            student=student,
            FEES_DATE=date.today(),
            amount=newfee
        )

        messages.success(request, "Fee Submitted Successfully!")
        return redirect("viewalldata")

    return render(request, "submitfee2.html", {"allfiled": student})

    
def PendingFEE(request):
    data = aa.objects.filter(remaningfee__gt=0)
    return render(request, 'PendingFEE.html', {"data": data})

    

def passoutview(request):
    return render(request,"passoutview.html")

def passoutstudent(request):
    data=bb.objects.all()
    pagedata={
        "varpage":data
    }    
    return render(request,"passoutstudent.html",pagedata)

def updateuserpass(request,regnodata):
    fatchingUpdatedata=bb.objects.get(registrationno=regnodata)
    gotet={
        "data":fatchingUpdatedata
    }
    try:
        if request.method=="POST":
            uid=fatchingUpdatedata.id
            rrrregnodata=fatchingUpdatedata.registrationno
            name=request.POST.get("name")
            fathername=request.POST.get("fathername")
            mothername=request.POST.get("mothername")
            mobno=request.POST.get("mobno")
            city=request.POST.get("city")
            message=request.POST.get("message")
            gender=request.POST.get("gender")
            course=request.POST.get("course")
            batchtime=request.POST.get("batchtime")
            Photo=request.FILES["Photo"]
            fee=request.POST.get("fee")
            remaningfee=request.POST.get("remaningfee")
            mydata=bb(registrationno=rrrregnodata,id=uid,name=name,fathername=fathername,mothername=mothername,
                      mobno=mobno,city=city,message=message,gender=gender,course=course,batchtime=batchtime,Photo=Photo,
                      fee=fee,remaningfee=remaningfee,)
            mydata.save()
            # mydata=fatchingUpdatedata.delete("{{data.id}}")
            url="/passoutstudent/"
            return HttpResponseRedirect(url)
    except:        
        pass
    
    return render(request,"updateuserpass.html",gotet)



def deletepassout(request,getid,Rpage): 
    get_id = get_object_or_404(bb, id=getid)
    
    # print(get_id,'--delte')
    if get_id.Photo:
        photo_path = os.path.join(settings.MEDIA_ROOT, str(get_id.Photo))
        if os.path.exists(photo_path):
            os.remove(photo_path)
    get_id.delete()
    
    messages.success(request, "Student Record Deleted Successfully!")
    return redirect(Rpage)

def certificate(request,registrationno):
    
    # onedata=bb.object.get(registrationno=registrationno)
    # pagedata={
    #     'data':onedata
    # }
    fatchingUpdatedata=bb.objects.get(registrationno=registrationno)
    gotet={
        "data":fatchingUpdatedata
    }
    
    print(fatchingUpdatedata.Photo)
    return render(request,'certificate.html',gotet)


# def Adminpanel(request):
#     if request.user.is_authenticated:
#         print("I am login")
#         return render(request,'base_admin.html')
#     else:
#         return redirect('/login')
    

@login_required(login_url="/login/")
def Adminpanel(request):
    return render(request,'base_admin.html')

# from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login ,logout as auth_logout

def login(request):

    if request.user.is_authenticated:
        return redirect('/Adminpanel')

    if request.method == 'POST':
        number = request.POST["number"]
        password = request.POST["password"]

        user = authenticate(username=number, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome {user.username}")
            return redirect('/Adminpanel')
        else:
            messages.warning(request, "Invalid Login")
            return redirect('/login')

    return render(request, 'login.html')


@login_required(login_url='/login/')
def signup(request):
    if request.user.is_authenticated:
         print('Please login and Tru again')
         return redirect('/login')
    
    if request.method=='POST':
        number= request.POST.get("number")
        password= request.POST.get("password")
        fname= request.POST.get("fname")
        lname= request.POST.get("lname")
        
        
        # --------------- SERCH INSIDE DATABASE ALREADY EXIST- START------------------------
        numbercheck=User.objects.filter(username=number).exists()
        if numbercheck== True:
            messages.warning(request,'NUMBER ALREADY REGISTERED')
            return redirect('/signup')
        # --------------- SERCH INSIDE DATABASE ALREADY EXIST- END--------------------------
        if len(number) != 10:
            messages.error(request,'10 digit menditory')
            return redirect('/signup')
        
        else:
            user= User.objects.create_user(username=number,password=password,email=number,first_name=fname,last_name=lname)
            user.first_name=fname
            user.last_name=lname
            user.save()
            messages.success(request,'User Registration is Successfully Submited')
            return redirect('/Adminpanel')
            
    return render(request,'signup.html')


def logout(request):
    auth_logout(request)
    messages.success(request, "You Successfully Logged Out")
    return redirect("/login")


