from django.http.response import HttpResponse
from django.shortcuts import render

def index (request):
    return render (request, "openforbusiness/index.html")

def about( request ):
    return render  (request, 'openforbusiness/about.html', {'mode': 8} )

def contact (request):
    return HttpResponse ("<h5>Contact Page, To Be Implementes</h5>")