from django.urls import path
from . import views
from django.contrib.auth import views as auth_views#this is imported to make the user authenticatoin 
from  .forms import login_form#this is imported to make the data that is requires to input from the user in the forms .py of this aopp to verify the data where login_form is the class to make the uuser input the authentication crecentials

app_name="core"
urlpattern=[
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path("signup/",views.signup , name="signup"),
    path("login/" , auth_views.LoginView.as_view(template_name="core/login.html" , authentication_form=login_form), name="login"),
]