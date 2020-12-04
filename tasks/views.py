from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def helloworld(request):
    return HttpResponse('helloworld')


def taskList(request):
    return render(request, 'tasks/list.html')


def yourname(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})
