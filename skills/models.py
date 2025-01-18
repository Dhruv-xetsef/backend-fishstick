from django.db import models
from django.contrib.auth.models import User
class category(models.Model):
    name=models.CharField(max_length=144)
    class Meta:
        ordering=("name",)#set the skills in the admin ppage by theit=r alphabetical order
        verbose_name_plural="Categories"#django admin page by default adds an s to the end of the object nm=ame so this make the name correct as categorys is wrong and categories is correct

    def __str__(self):
        return self.name#by default the thing will be added like category(0) but this command will make them to be set by their name that we have given
class data(models.Model):
    category=models.ForeignKey(category,related_name="users",on_delete=models.CASCADE)#on the delete of the item all the related information also gets deleted this means then when a user deletes his id al t=his belongingings like his skills etc will be deleted from his profile
    name=models.CharField(max_length=144)
    description=models.TextField(blank=True,null=True)
    skills=models.CharField(max_length=144)
    speciallity=models.TextField()
    price=models.FloatField()
    photo=models.ImageField(upload_to="user_images",blank=True,null= True)#here the blank and the null are true so tha the user has the choie to ni=ot to upload the image as the image filed can be left empt
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name="users",on_delete=models.CASCADE)
    is_sold = models.BooleanField(default=False)  # Add this line
    def __str__(self):
        return self.name#stores the user data by
# Create your models here.
