from django.shortcuts import render, HttpResponse
from .models import feedback ,Contact,Event,Sports_Plan,Sports,Admission

# Create your views here.


#### more feedback

def more_feedback(request):
    feedback_list=feedback.objects.all()
    context={
        "feedback_key": feedback_list
    }
    return render(request,'sa_app/html/all_feedbacks.html',context)

def home(request):
    feedback_list=feedback.objects.order_by('-date')[:3]
    context={
        "feedback_key": feedback_list
    }
    return render(request, 'sa_app/html/home.html',context)

def about(request):
    return render(request,'sa_app/html/about_us.html')

def feedback1(request):
    if request.method == 'GET':
        return render(request,'sa_app/html/feedback.html')
    if request.method == 'POST': 

        ## fetching data from html controls 

        user_name= request.POST["name"]   
        user_email=request.POST["email"]

        fdlist=feedback.objects.filter(email=user_email)

        if len(fdlist)>0:
             return render(request,'sa_app/html/feedback.html')
            

        else:
              user_rating=request.POST["rating"]
              user_remark=request.POST["remark"]
        # print(user_name,user_email,user_rating,user_remark)
        

        # creating object of feedback Model

        feedback_object=feedback(name=user_name,email=user_email,remarks=user_remark,rating=user_rating)

        ## save the objects 
        feedback_object.save()
        return render(request,'sa_app/html/feedback.html')
        
def sport(request):
    sport_list=Sports.objects.all()
    context = {
        "sport_key" : sport_list
    }
    return render (request, 'sa_app/html/sports.html',context)


def contact(request):
    if request.method =='GET':
        return render(request,'sa_app/html/contact_us.html')
    if request.method =='POST':
        

        ## FETCHING DATA FROM HTML CONTROLS 

        user_name=request.POST["name"]
        user_email=request.POST["email"]
        user_number=request.POST["number"]
        user_question=request.POST["question"]
        # print(user_name,user_email,user_number,user_query)


        ### CREATING OBJECT OF CONTACT MODEL

        contact_object=Contact(name=user_name,email=user_email,phone=user_number,question=user_question)

        ## SAVE THE OBJECTS

        contact_object.save()
        return render(request,'sa_app/html/contact_us.html')
         
        
        
def event_update(request):


    event_list=Event.objects.all()  ## quivalent to rdbms query  select * from event
    # print(type(event_list))

    ### how to send the data from view to template 

    context={
        "events_key": event_list
    }


    return render(request,'sa_app/html/events_updates.html',context)

# def view_feedback1(request):
#     view_feedback1=feedback.objects.all()
#     view_context={
#         "feedback_key": view_feedback1
#     }
#     return render (request,'sa_app/html/feedback.html',view_context)


###function for charges

def plan(request):
    plan_list=Sports_Plan.objects.all()
    context={"plan_key": plan_list}
    return render(request,'sa_app/html/plans.html',context)


##### function for admission 

def admission(request):
    if request.method=='GET':
        plan_list = Sports_Plan.objects.all()
        sports_list = Sports.objects.all()
        context={'plan_key' : plan_list, 'sports_key':sports_list}
        return render(request,"sa_app/html/admission.html",context)
    if request.method=='POST':
        sname=request.POST["name"]
        semail=request.POST["email"]
        sphone=request.POST["phone"]
        smother_name=request.POST["mother_name"]
        sfather_name=request.POST["father_name"]
        salternate_no=request.POST["alternate_no"]
        scity=request.POST["city"]
        sage=request.POST["age"]
        sgender=request.POST["gender"]
        sdate_of_birth=request.POST["dob"]
        sphoto=request.FILES.get("photo")
        ssports_plan=request.POST["sports_plan"]
        ssports_name=request.POST["sports_name"]
        sdate=request.POST["date"]
        smode=request.POST["mode"]
        fee=request.POST["fee"]
        stransaction_no=request.POST["transaction"]
        Admission_obj=Admission(fees=fee,name=sname,email=semail,phone=sphone,mother_name=smother_name,father_name=sfather_name,alternate_no=salternate_no,city=scity,age=sage,gender=sgender,date_of_birth=sdate_of_birth,photo=sphoto,sports_plan=ssports_plan,sports_name=ssports_name,date=sdate,mode=smode,transaction_no=stransaction_no)
        Admission_obj.save()
        return render (request,"sa_app/html/admission.html")
    
    
