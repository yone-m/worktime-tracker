from django.urls import path

from . import views

urlpatterns = [
    path("", views.work_list_today, name="work_list_today"),
    path("month/", views.work_list_month, name="work_list_month"),
    path("create/", views.work_create, name='work_create')
]