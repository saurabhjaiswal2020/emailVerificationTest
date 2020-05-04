from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

@login_required()
def dashboard(request):
    return render(request, 'first_app/dashboard.html')

class CBView(TemplateView):
    template_name = 'first_app/contact.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PageData'] = "This is contact Page"
        return context