from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView
import requests
import os
import subprocess
import re

from myapp import create_file

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def dashboard(request):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    email = request.GET.get('email', default="admin@gmail.com").strip()

    if email == 'admin@gmail.com':
        status = "Provide an Email"
    else:
        if (re.search(regex, email)):
            status = "Email is Valid"
            create_file('valid_emails.txt', email)
        else:
            create_file('invalid_emails.txt', email)
            status = "Email is InValid"


    page_data = {'response': status}

    # p = subprocess.Popen('python myapp.py', stdout=subprocess.PIPE, shell=True)

    return render(request, 'first_app/dashboard.html', context=page_data)


class CBView(TemplateView):
    template_name = 'first_app/contact.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PageData'] = "This is contact Page"
        return context