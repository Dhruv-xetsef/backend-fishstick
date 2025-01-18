from django.urls import path 
from . import views
app_name="conversations"
urlpattern=[
    path("", views.inbox , name="inbox"),
    path("<int:pk>/", views.detail , name="detail"),#assign the primary to the details pae which shows the details of the conversatiopage of the app
    path("new/<int:item_pk>/", views.new_conversation , name="new")#this is the function to to add noew conersation to the primary key
]