from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('category/', views.categoryview, name='categories'),
    path('unit/', views.unitview, name='units'),
    path('item/', views.itemview, name='items'),
    path('supplier/', views.Supplierview, name='suppliers'),
    path('order/', views.Orderview, name='orders'),
    path('employee/', views.Employeeview, name='employees'),
    path("", views.home, name="home"),
]
