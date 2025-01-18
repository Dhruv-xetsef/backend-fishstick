from django.shortcuts import render , get_object_or_404 , redirect   # this the commmand to use the get error 404 page when ever a page isx noe available or there is the error in the file
from django.contrib.auth.decorators import login_required# this is impoted so thatt the person trying to use the converstions page has to login first to use the page without the logi the use of the conversation pagr becoanrs not possible
from skills.models import data
from .forms import conversation_message_form
from .models import conversation
@login_required #this commannd mandates ythe loigin in requred 6
def new_conversations(request , data_pk):
    datas= get_object_or_404(data , pk= data_pk)
    if datas.created_by == request.user:
        return redirect("dashboard:index")
    conversations= conversation.objects.filter(datas= datas).filter(members__in=[request.user.id])
    if conversations:
        return redirect("conversation:detail", pk= conversations.first().id)
    if request.method =="POST":
        form = conversation_message_form(request.POST)
        if form.is_valid():
            conversations= conversation.objects.create(datas=datas)
            conversation.members.add(request.user)
            conversation.members.add(datas.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversations
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=data_pk)
    else:
        form = conversation_message_form()
    
    return render(request, 'conversation/new.html', {
        'form': form
    })

@login_required
def inbox(request):
    conversations = conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })

@login_required
def detail(request, pk):
    conversations = conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = conversation_message_form(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversations
            conversation_message.created_by = request.user
            conversation_message.save()

            conversations.save()

            return redirect('conversation:detail', pk=pk)
    else:
        form = conversation_message_form()

    return render(request, 'conversation/detail.html', {
        'conversation': conversations,
        'form': form
    })


# Create your views here.
