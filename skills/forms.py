from django import forms 
from .models import data
INPUT_CLASSES="w-full py-4 px-6 rounded-xl border"
class new_skill_form(forms.ModelForm):
    class Meta:
        model=data
        fields=("category","name","description","skills","speciallity","price","photo")
        widgets={
            "category" : forms.select(attrs={
                "class":INPUT_CLASSES
                }),
            "name":forms.TextInput(attrs={
                "class" : INPUT_CLASSES,
                
            
        }),
        "description":forms.Textarea(attrs={
            "class":INPUT_CLASSES
        }),
        "skills":forms.TextInput(attrs={
            "class":INPUT_CLASSES
        }),
        "speciallity":forms.Textarea(attrs={
            "class":INPUT_CLASSES
        }),
        "price":forms.NumberInput(attrs={
            "class":INPUT_CLASSES
        }),
        "photo":forms.FileInput(attrs={
            "class":INPUT_CLASSES
        })
        }
class edit_skill_form(forms.ModelForm):
    class Meta:
        model=data
        fields=("category","name","description","skills","speciallity","price","photo")
        widgets={
            "category" : forms.select(attrs={
                "class":INPUT_CLASSES
                }),
            "name":forms.TextInput(attrs={
                "class" : INPUT_CLASSES,
                
            
        }),
        "description":forms.Textarea(attrs={
            "class":INPUT_CLASSES
        }),
        "skills":forms.TextInput(attrs={
            "class":INPUT_CLASSES
        }),
        "speciallity":forms.Textarea(attrs={
            "class":INPUT_CLASSES
        }),
        "price":forms.NumberInput(attrs={
            "class":INPUT_CLASSES
        }),
        "photo":forms.FileInput(attrs={
            "class":INPUT_CLASSES
        })
        }