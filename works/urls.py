from django.urls import path

from . import views

app_name = 'work'

urlpatterns = [
    path("list/", views.WorkListToday.as_view(), name="work_list_today"),
    path("month/", views.WorkListMonth.as_view(), name="work_list_month"),
    path("create/", views.WorkCreate.as_view(), name='work_create')
]