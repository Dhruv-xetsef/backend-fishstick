from django.shortcuts import render , redirect
from skills.models import category, data
from .forms import signup_form#import the data of the signup_forms class from the forms.py
def index(request):
    skills=data.objects.filter(is_sold=False)#shiw the items that we added to the index of the hom page
    categories=category.objects.all()

    return render(request,'core/index.html',{
        "categories" : categories,
        "skills": skills,

    })
def contact(request):
    return render(request,'core/contact.html')
def signup(request):
    if request.method == "POST":
        form = signup_form(request.POST)#here the signup_form is used to take the dat from the forms.py files where data is stores in the clas signup_form class
        if form.is_valid():
            form.save()#this is to save the form data
            return redirect("/login/")#make the user to redirect to the login page for the purpose of login after the cration of the account is succesfully completed
    else:
        form =signup_form()
    return render(request , "core/signup.html",{#here the return functio is used to return the page to the signup form
        "form" :form
        })
# Create your views here.
