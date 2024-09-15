from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Work
from .forms import WorkForm
import datetime

def work_list_today(request):
    today = datetime.date.today() 
    today_str = today.strftime('%Y/%m/%d')
    works = Work.objects.filter(created_at__date=today)
    return render(request, 'works/work_list.html', {'works': works, 'today': today_str})

def work_list_month(request):
    this_month = datetime.date.today().month
    #this_month_str = this_month.strftime('%m')
    works = Work.objects.filter(created_at__date__month=this_month)
    return render(request, 'works/work_list_month.html', {'works': works, 'this_month': this_month})

def work_create(request):
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work_list_today')
    else:
        form = WorkForm()
    return render(request, 'works/work_form.html', {'form': form})