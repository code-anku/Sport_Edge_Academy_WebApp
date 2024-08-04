from django.db import models
from django.utils import timezone

# Create your models here.
# feedback model

class feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    remarks = models.TextField()
    rating = models.CharField(max_length=1)
    date = models.DateField(default=timezone.now)


# contact model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10) 
    question = models.TextField()
    date = models.DateField(default = timezone.now)



class Event(models.Model):
    event_name=models.CharField(max_length=55,primary_key=True)
    event_venue=models.CharField(max_length=100,default="Auditorium")
    event_date = models.DateField(default = timezone.now)
    event_description=models.TextField()
    event_pic=models.FileField(max_length=100,upload_to="sa_app/event_images",default="")


class Coach(models.Model):
    coach_id=models.CharField(max_length=55,primary_key=True)
    password=models.CharField(max_length=55)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    gender=models.CharField(max_length=6)
    city= models.CharField(max_length=55)
    address=models.CharField(max_length=55)
    experience=models.TextField()
    about_coach=models.TextField()
    area_of_interest=models.TextField()
    date = models.DateField(default = timezone.now)


class Student(models.Model):
    Student_id=models.CharField(max_length=55,primary_key=True)
    password=models.CharField(max_length=55)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    gender=models.CharField(max_length=6)
    city= models.CharField(max_length=55)
    address=models.CharField(max_length=55)
    date = models.DateField(default = timezone.now)


class Sports_Plan(models.Model):
    plan_name=models.CharField(max_length=50, primary_key=True)
    plan_duration=models.CharField(max_length=100)
    facilities=models.TextField(max_length=500)
    charges=models.IntegerField()

class Sports(models.Model):
    sports_name=models.CharField(max_length=20,primary_key=True)
    sports_type=models.CharField(max_length=20)
    sports_minimum_duration=models.CharField(max_length= 20)
    Sports_charges=models.CharField(max_length=10)
    sports_dress=models.FileField(max_length=100,upload_to="sa_app/sports_images")
    sports_image=models.FileField(max_length=100,upload_to="sa_app/sports_img",default="")
    sports_description=models.TextField(max_length=500)


class Admission(models.Model):
    student_id=models.CharField(max_length=10,default="")
    password=models.CharField(max_length=50,default="")
    status=models.CharField(max_length=10,default="")
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=10)
    mother_name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    alternate_no=models.CharField(max_length=10)
    city=models.CharField(max_length=10)
    age=models.CharField(max_length=2)
    gender=models.CharField(max_length=1)
    date_of_birth=models.CharField(max_length=10)
    photo=models.FileField(max_length=100, upload_to="sa_app/student_image",default="")
    sports_plan=models.CharField(max_length=10)
    sports_name=models.CharField(max_length=10)
    date=models.CharField(max_length=10)
    fees=models.CharField(max_length=10,default="")
    mode=models.CharField(max_length=10,default="")
    transaction_no=models.CharField(max_length=32,default="")



    # coach asssign model 

    # class AssignCoach(models.Model):
    #     admission=models.ForeignKey(Admission,on_delete=models.DO_NOTHING)
    #     trainer=models.ForeignKey(Trainer,on_delete=models.DO_NOTHING)
    #     status=models.BooleanField(default=False)