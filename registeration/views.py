from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import user,system
from django.template import loader
from django.http import Http404
from registeration.forms import LoginForm
from registeration.models import user,system
from django.conf import settings
import urllib
import requests
import json
from django.contrib import messages
# Create your views here.


def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    ip_cnt = system.objects.filter(ip=visitor_ip_address(request)).count()
    context = {'site_key': settings.RECAPTCHA_SITE_KEY,'ip_cnt':ip_cnt}
    return render(request,'registeration/index.html',context)



def register(request):

    name = "not Register"
    ip = system()
    ip.ip = visitor_ip_address(request)
    ip.save()
    if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid() and MyLoginForm.clean_message():
         ip_cnt = system.objects.filter(ip=visitor_ip_address(request)).count()
         if ip_cnt > 3 :
             recaptcha_response = request.POST.get('g-recaptcha-response')
             url = 'https://www.google.com/recaptcha/api/siteverify'
             values = {
                'secret': settings.RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
                 }
             data = urllib.parse.urlencode(values).encode('utf-8')
             req = urllib.request.Request(url, data)
             response = urllib.request.urlopen(req)
             result = json.load(response)
              # ''' End reCAPTCHA validation '''

             if result['success']: 
                 new_user = user()
                 new_user = MyLoginForm.clean_message()
                 name = MyLoginForm.cleaned_data['name']
                 new_user.save()
             else :
                 messages.error(request,"Recaptcha doesnot match")
                 return render(request,'registeration/index.html',{"name" : name,'ip_cnt':ip_cnt})
         else :
              new_user = user()
              new_user = MyLoginForm.clean_message()
              name = MyLoginForm.cleaned_data['name']
              new_user.save()

    else:
      MyLoginForm = LoginForm()

    return render(request, 'registeration/loggedin.html', {"name" : name})



