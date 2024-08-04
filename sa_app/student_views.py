from django.shortcuts import render, HttpResponse, redirect
from.models import Student
from django.contrib import messages


###EDIT PROFILE CODE
def student_edit_profile(request):
     if "session_key" not in request.session.keys():
         return redirect("student_login")
     if request.method=="GET":
         id=request.session["session_key"]
         obj=Student.objects.get(Student_id=id)
         context={
        "obj_key":obj
        }
         return render (request,'sa_app/student/student_edit_profile.html',context)
     if request.method == 'POST':
        nm=request.POST["name"]
        em=request.POST["email"]
        ph=request.POST["phone"]
        ct=request.POST["city"]
        add=request.POST["address"]
        id=request.session["session_key"]
        obj=Student.objects.get(Student_id=id)
        obj.name=nm
        obj.email=em
        obj.phone=ph
        obj.city=ct
        obj.address=add
        obj.save()
        context={
        "obj_key":obj
        }
        return render (request,'sa_app/student/student_edit_profile.html',context)




##FUNCTION FOR HOME

def student_home(request):
     if "session_key" not in request.session.keys():
         return redirect("student_login")
     id=request.session["session_key"]
     obj=Student.objects.get(Student_id=id)
     context={
        "obj_key":obj
    }
     return render (request,'sa_app/student/student_home.html',context)

def login(request):

    if request.method == 'GET':
        return render (request,'sa_app/student/student_login.html')
    if request.method=='POST':
        user_id=request.POST["Student_id"]
        user_pass=request.POST["password"]
        student__list=Student.objects.filter(Student_id=user_id,password=user_pass)
        size=len(student__list)
        if size>0:
            print("user exits")

            ###bindingig id in session 

            request.session["session_key"]=user_id
            obj=Student.objects.get(Student_id=user_id)
            context={
                "obj_key":obj
            }
            return render (request ,'sa_app/student/student_home.html', context)
        else:
            messages.error(request,"invalid  Credentials")
        return render (request,'sa_app/student/student_login.html')


def registration(request):

    if request.method == 'GET':
        
        return render (request,'sa_app/student/student_registration.html')
    if request.method == 'POST':
        S_id=request.POST["user_id"]
        S_pass=request.POST["user_pass"]
        S_name=request.POST["name"]
        S_father_name=request.POST["father_name"]
        S_mother_name=request.POST["mother_name"]
        S_email=request.POST["email"]
        S_phone=request.POST["phone"]
        S_gender=request.POST["gender"]
        S_city=request.POST["city"]
        S_address=request.POST["address"]

        reg_obj=Student(Student_id=S_id,password=S_pass,name=S_name,father_name=S_father_name,mother_name=S_mother_name,email=S_email,phone=S_phone,gender=S_gender,city=S_city,address=S_address)
        reg_obj.save()
        return render (request,'sa_app/student/student_registration.html')


####  logout function 

def logout(request):
     if "session_key" not in request.session.keys():
         return redirect("student_login")
     request.session.flush()  ### clearing all the values bind in that session 
     return redirect ("student_login")  ## name of the view
