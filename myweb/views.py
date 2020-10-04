from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    return render(request, 'web.html')

def recent(request):
    return HttpResponse('<h1>HTTP Response</h1>')
