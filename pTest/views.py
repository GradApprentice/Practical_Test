from django.shortcuts import render
from django.http import HttpResponse
from pTest import views
from pTest.models import News

def index(request):
    context_dict = {}
    context_dict['newsList'] = News.objects.order_by('-newsDate')
    return render(request, 'pTest/index.html', context=context_dict)