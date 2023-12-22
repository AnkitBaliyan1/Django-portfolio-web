from django.contrib import admin
from django.urls import path
from . import views

app_name = "mywebsite"
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('academics/', views.academics, name="academics"),
    path('machine-learning/',  views.machinelearning, name='machinelearning'),
    path('SQL/',  views.sql, name='sql'),
    path('bi-tools/',  views.bitools, name='bitools'),
    path('llm/',  views.llm, name='llm'),
    path('upcoming/',  views.upcoming, name='upcoming'),
    path('contact/', views.contact_view, name='contact_view'),
]
