from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.department_list, name='department_list'),
    path('login/', views.Login_View, name='login'),
    # Other URL patterns...
]