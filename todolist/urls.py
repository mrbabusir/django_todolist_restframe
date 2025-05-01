from django.urls import path, include
from .views import *
urlpatterns = [
    path('todolist/',todolist_list),
    path('todolist/<int:id>/', todolist_detail),
]