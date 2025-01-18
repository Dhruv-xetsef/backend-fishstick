from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm#imports the authentication form and the user creation form to verify the existance of the user and to create a user
from django.contrib.auth.models import User
class login_form(AuthenticationForm):
    User_name=forms.CharField(widget=forms.TextInput(attrs={
        "placeholder" : "Enter your user name",
        "class" : "w-full py-6 rounded-xl"#this is a html code for the creation of  the look of the login box tyope to authenticate and to create the users                                                            
    }))
    passwords= forms.Charfield(widget= forms.PasswordInput(attr={
        "placeholder" : "Enter your password",#make the user to input the password in the placeholder
        "class" : "w-full py-4 px-6 rounded-xl" #this is a html code for the creation of  the look of the login box tyope to authenticate and to create the users
    }))
class signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ("user_name" , "email" , "password1" , "password2" )
    user_name = forms.CharField(widget=forms.TextInput(attrs={#this is the constraint used to create the user name of the client side server
        "placeholder" : "Enter your name",
        "class" :"w-full py-4 px-6 rounded-xl"
    }))
    email= forms.CharField(widget=forms.Emailinput(attrs={
        "placeholder": "enter your email",
        "class"  : "w-full py-4 px-6 rounded-xl"
    }))
    password1= forms.CharField(widget = forms.PasswordInput(attrs={
        "placeholder" : "enter your password",
        "class" : "w-full py-4 px-6 rounded-xl"
    }))
    password2= forms.CharField(widget = forms.PasswordInput(attrs={
        "placeholder" :"repeat the pasword that you entered earlier",
        "class" : "w-full py-4 px--6 rounded-xl"
    }))


