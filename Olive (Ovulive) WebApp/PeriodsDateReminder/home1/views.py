from django.shortcuts import render,HttpResponse, redirect
from django.conf import settings
from datetime import date, datetime
from django.template.loader import render_to_string
from django.http import request
from home.models import Person
from home.views import home
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives


# Create your views here.

def sender(request):
    today=datetime.now().strftime('%d')
    month_now=datetime.now().strftime('%m')
    data= Person.objects.all()
    for item in data.values('id','sender','receiver','period','email','month'):
        period= item['period'].strftime('%d')
        receiver_email =item['email']
        id_user=item['id']
        month_in_pd=item['month']
        sender=item['sender'].split(" ")[0]
        receiver=item['receiver'].split(" ")[0]
        if period == today and month_in_pd< int(month_now):
            context={
                "receiver":receiver.capitalize(),
                "sender":sender.capitalize()
            }
            print(f" Period details:{context}")
            html_content = render_to_string("email_temp.html", context)
            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(
                f" Periods Date is coming {receiver.capitalize()}",
                text_content,
                "yashikajotwani <yashikajothwani39@gmail.com>",
                [receiver_email]
            )
            email.attach_alternative(html_content, "text/html")
            email.send()
            user = Person.objects.get(id=id_user)
            user.month = month_now
            user.save()
    return redirect(home)


def email_temp(request, sender=None, receiver=None):
    if not sender or sender == None or not receiver or receiver == None:
        return render(request, "index.html")
    else:
        context = {
            "sender": sender,
            "receiver": receiver
        }
        return render(request, "wish.html", context)
   


def Task():
    return sender(request)