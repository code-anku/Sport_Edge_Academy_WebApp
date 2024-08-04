from django.shortcuts import render,redirect
from.models import Coach
from django.contrib import messages



# def login(request):

#     if request.method == 'GET':
        
#         return render (request,'sa_app/coach/coach_login.html')
    
def login(request):

    if request.method == 'GET':
        return render (request,'sa_app/coach/coach_login.html')
    if request.method=='POST':
        user_id=request.POST["coach_id"]
        user_pass=request.POST["password"]
        coach__list=Coach.objects.filter(coach_id=user_id,password=user_pass)
        size=len(coach__list)
        if size>0:
            # print("user exits")

            ###bindingig id in session 

            request.session["session_key"]=user_id
            obj=Coach.objects.get(coach_id=user_id)
            context={
                "obj_key":obj
            }
            return render (request ,'sa_app/coach/coach_home.html', context)
        else:
            messages.error(request,"invalid  Credentials")
        return render (request,'sa_app/coach/coach_login.html')
    
    
def coach_edit_profile(request):
     if "session_key" not in request.session.keys():
         return redirect("coach_login")
     if request.method=="GET":
         id=request.session["session_key"]
         obj=Coach.objects.get(coach_id=id)
         context={
        "obj_key":obj
        }
         return render (request,'sa_app/coach/coach_edit_profile.html',context)
     if request.method == 'POST':
        nm=request.POST["name"]
        em=request.POST["email"]
        ph=request.POST["phone"]
        ct=request.POST["city"]
        add=request.POST["address"]
        id=request.session["session_key"]
        obj=Coach.objects.get(coach_id=id)
        obj.name=nm
        obj.email=em
        obj.phone=ph
        obj.city=ct
        obj.address=add
        obj.save()
        context={
        "obj_key":obj
        }
        return render (request,'sa_app/coach/coach_edit_profile.html',context)
    
def coach_home(request):
     if "session_key" not in request.session.keys():
         return redirect("coach_login")
     id=request.session["session_key"]
     obj=Coach.objects.get(coach_id=id)
     context={
        "obj_key":obj
    }
     return render (request,'sa_app/coach/coach_home.html',context)

def coach_view_profile(request):
     if "session_key" not in request.session.keys():
         return redirect("coach_login")
     if request.method=="GET":
         id=request.session["session_key"]
         obj=Coach.objects.get(coach_id=id)
         obj.save()
         context={
        "obj_key":obj
        }

     return render (request,'sa_app/coach/coach_view_profile.html',context)

####  logout function 

def logout(request):
    if "session_key" not in request.session.keys():
         return redirect("coach_login")
    request.session.flush()  ### clearing all the values bind in that session 
    return redirect ("coach_login")  ## name of the view

    