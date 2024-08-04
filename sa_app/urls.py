from django.urls import path
from . import views,student_views,coach_views

urlpatterns = [
    path("", views.home, name="home"),
    path("about_us/", views.about, name="about"),
    path("feedback/", views.feedback1, name="feedback"),
    path("contact_us/", views.contact, name="contact"),
    path("student_login/",student_views.login,name="student_login"),
    path("student_registration/",student_views.registration,name="student_registration"),
    path("coach_login/",coach_views.login,name="coach_login"),
    path("coach_home/",coach_views.coach_home,name="coach_home"),
    path("coach_edit_profile/",coach_views.coach_edit_profile,name="coach_edit_profile"),
    path("events/",views.event_update,name="events"),
    path("more_feedback/",views.more_feedback,name="more_feedback"),
    path("student_home/",student_views.student_home,name="student_home"),
    path("student_edit_profile/",student_views.student_edit_profile,name="student_edit_profile"),
    path("coach_view_profile/",coach_views.coach_view_profile,name="coach_view_profile"),
    path("plans/",views.plan,name="plans"),
    path("coach_logout/",coach_views.logout,name="coach_logout"),
    path("student_logout/",student_views.logout,name="student_logout"),
    path("sports/",views.sport,name="sports"),
    path("admission/",views.admission,name="admission"),
    




]