from django.shortcuts import render
from django.contrib.messages.api import error
from django.shortcuts import render
from .models import Person
from .resources import PersonResource
from django.contrib import messages
from tablib import Dataset
from datetime import datetime

# Create your views here.
def home(request):
    return render(request,'index.html')

def add_form(request):
    if request.method == 'POST':
        if request.POST.get('sender') and request.POST.get('receiver') and request.POST.get('email') and request.POST.get('period'):
            sender = request.POST['sender']
            receiver = request.POST['receiver']
            email = request.POST['email']
            period = request.POST['period']
            month_now = int(datetime.now().strftime("%m"))-1
            person = Person(
                sender=sender,
                receiver=receiver,
                email=email,
                period=period,
                month=month_now
            )
            person.save()
            messages.success(
                    request, "We have successfully added the data on our server.")
            return render(request, "form.html")
        else:
            error = {
                "error": 'One or more fields is missing.'
            }
            return render(request, "form.html", error)
    return render(request, "form.html")