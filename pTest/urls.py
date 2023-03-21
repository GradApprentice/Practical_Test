from django.urls import path
from pTest import views

app_name = 'pTest'
    urlpatterns = [
    path('', views.index, name='index'),
]