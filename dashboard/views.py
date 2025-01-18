from django.shortcuts import render , get_object_or_404
from django.contrib.auth.decorators import login_required
from skills.models import data
@login_required
def index(request):
    datas= data.objects.filter(created_by=request.user)
    return render(request,"dashboard/index.html",{"datas":datas})


# Create your views here.
