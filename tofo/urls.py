from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("",index),
    path("contact",contact),
    path("task/<pk>",mark_as_completed),
    path("create-task",create_task),
    path("task/<pk>/edit",update_task),
    path("task/<pk>/delete",delete_task),
    ]
