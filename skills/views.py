from django.shortcuts import render,get_object_or_404, redirect
from .models import data ,category
from .forms import new_skill_form , edit_skill_form
from django.contrib.auth.decorators import login_required
from django.db.models import Q
def skills(request):
    query=request.GET.get("query" , "")
    category_id = request.GET.get("category", None)
    categories = category.objects.all()

    datas= data.object.filter(is_sold=False)
    if category_id:
        datas = datas.filter(category_id=category_id)
    if query:
        datas = datas.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'skills/skills.html', {'datas': datas, 'categories': categories})


def detail(request , pk):#to make the database show the item based on its primay key
    datas = get_object_or_404(data, pk=pk)#show error 404 whwn not available and primary key based on the object
    related_datas = data.objects.filter(category=datas.category , is_sold=False).exclude(pk=pk)[:4]

    return render(request, 'skills/detail.html', {
        'datas': datas, 
        "related_datas": related_datas })#render the html file and pass th
# Create your views here.
@login_required
def new(request):
    if request.method == 'POST':
        form = new_skill_form(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.owner = request.user
            data.save()
            return redirect('skills')
    else:
        form = new_skill_form()
    return render(request, 'skills/new.html', {'form': form , 'title': 'New Skill'})

@login_required
def edit(request, pk):
    data = get_object_or_404(data, pk=pk , created_by=request.user)
    if request.method == 'POST':
        form = edit_skill_form(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('data:detail', pk=data.id)
    else:
        form = edit_skill_form(instance=data)
        
    return render(request, 'skills/new.html', {'form': form , 'title': 'Edit Skill'})
@login_required
def delete(request, pk):
    data = get_object_or_404(data, pk=pk , created_by=request.user)
    data.delete()
    return redirect('dashboard:index')

