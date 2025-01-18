from django.urls import path
from . import views
app_name="skills"
urlpatterns=[
    path("<int:pk>/", views.detail , name="detail"),
    path("", views.skills ,  name="skills"),
    path("create/", views.create ,  name="create"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/edit/", views.edit, name="edit"),

]