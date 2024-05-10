from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
import requests
# Create your views here.


def home(request):
    projects = Project.objects.all()
    skillTopic = SkillTopic.objects.all()
    context = {'projects': projects,
               'skilltopics' : skillTopic
                }
    return render(request, '../templates/main.html' , context)


def contact(request):
    if request.method == 'POST':
        print("dm thanh duy")
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')

        full_msg = f"""
        Hello, my name is {name}, My email : {email}
        {message}
        """

        bot_token = '7046829707:AAHt9d9m8kV3lYNu6smrxNt2sN57GTeLt8A'
        chat_id = '6505326895'


        send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={full_msg}'

        requests.get(send_text)

        return HttpResponseRedirect('thank_you')

    return render(request, 'contact.html')


