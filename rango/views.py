from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'hello world!'}
    return render(request, 'rango/index.html', context=context_dict)

# Create your views here.
