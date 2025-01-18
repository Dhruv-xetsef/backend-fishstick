from django.contrib import admin
from .models import Conversation , Conversation_message# imports conversationsa na dthe conversations message from the models.py of the conversastion filr or you can say thois folder the purpose of the admin site registert
admin.site.register(conversation)
admin.site.register(conversation_message)

# Register your models here.
