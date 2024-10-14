from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

# Create your views here.
class AppLoginView(LoginView):
    template_name = "other/login.html"
    
    def get_success_url(self):
        return reverse_lazy("work:work_list_today")