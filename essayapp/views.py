from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Essay1

# Create your views here.
def index(request):
    return render(request,'index.html')
def submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        roll_no = request.POST['roll_no']
        college = request.POST['college']
        topic = request.POST['topic']
        essay = request.POST['essay']
        
        essay = Essay1(name=name,roll_no=roll_no,college=college,topic=topic,essay=essay)
        #user =User.objects.create_user(first_name=first_name,last_name=last_name,username=username)

        essay.save();
        messages.info(request,'Succefully submited')
        return redirect('index.html')
    else:
        return render(request,'submit.html')