from django import forms
from .models import conversation_message
class conversation_message_form(forms.ModelForm):#creates a form of the user conversation mesags that are imported from the models.py of this 
    class Meta:
        model = conversation_message
        fields = ("content",)
        widget ={
            "content" : forms.Texxtarea(attrs={
                "class" :"w-full py-4 px-6 rounded-xl border"
            })
        }