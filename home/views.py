from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail

# Create your views here.


def one(request):
    context = {}
    return render(request, 'new.html', context)




