from django.db import models
from django.contrib.auth.models import User
from skills.models import data
class conversation(models.Model):#define a class mconversation to store the data of the user conversations so that the chat ystem ca have access to the chat suport of te maplatform 

    skill= models.ForeignKey( data , related_name="conversations" , on_delete = models.CASCADE)
    members = models.ManyToManyField(User, related_name="conversations")
    created_at = models.DateTimeField(auto_now_add= True)
    modified_at= models.DateTimeField(auto_now= True)
    class Meta:
        ordering = ("- modiefied at ")#add the given string if the thing is modified after its creation
class conversation_mesaage(models.Model):
    conversation= models.ForeignKey(conversation , related_name="message" , on_delete= models.CASCADE)
    content= models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    created_by = models.Foreignkey(User, related_name="created_message" , on_delete= models.CASCADE) 
    #Create your models here
