from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myblog.models import Users


def index(request):

    u = Users.objects.all()
    return  HttpResponse(u)
    #return HttpResponse(u'欢迎使用LiyyCMS')
    #return  render(request,'home.html')

