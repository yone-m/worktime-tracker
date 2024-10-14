from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Work
from .forms import WorkForm
from datetime import datetime

class WorkListToday(LoginRequiredMixin, generic.ListView):
    model = Work
    context_object_name = "works"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = datetime.today().strftime("%Y年%m月%d日")
        return context
    
    def get_queryset(self):
        return super().get_queryset()
    
    
class WorkListMonth(LoginRequiredMixin, generic.ListView):
    model = Work
    context_object_name = "monthly_works"
    template_name = "work/work_list_month.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["month"] = str(datetime.today().month)
        return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset

class WorkCreate(LoginRequiredMixin, generic.CreateView):
    model = Work
    form_class = WorkForm
    success_url = reverse_lazy('work:work_list_today')
    
    def form_valid(self, form):
        today_str = datetime.today().strftime("%Y/%m/%d")
        input_start_time = self.request.POST.get("start_time")
        input_end_time = self.request.POST.get("end_time")
        form.instance.start_datetime = datetime.strptime(today_str + " " + input_start_time + ":00", "%Y/%m/%d %H:%M:%S")
        form.instance.end_datetime = datetime.strptime(today_str + " " + input_end_time, "%Y/%m/%d %H:%M:%S")
        form.save()
        return super().form_valid(form)
