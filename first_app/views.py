from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView
import requests
import os
import subprocess
import re

from myapp import *

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def dashboard(request):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    email = request.GET.get('email', default="").strip()
    domain = email.split('@')[1]

    if email == '':
        status = "Provide an Email"
    else:
        if (re.search(regex, email)):
            status = "Email is Valid"
            disposable = disposable_check(domain)
            create_file('valid_emails.txt', email)
            print(disposable)
        else:
            create_file('invalid_emails.txt', email)
            disposable = disposable_check(domain)
            status = "Email is InValid"


    page_data = {
        'email': email,
        'domain': domain,
        'status': status,
        'disposable': disposable
    }

    # p = subprocess.Popen('python myapp.py', stdout=subprocess.PIPE, shell=True)

    return render(request, 'first_app/dashboard.html', context=page_data)


class CBView(TemplateView):
    template_name = 'first_app/contact.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PageData'] = "This is contact Page"
        return context