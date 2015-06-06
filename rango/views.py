from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from rango.models import Category

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage':'I am bold font from the context'}
    return render_to_response('rango/index.html',context_dict,context)
