#from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "I am bold font from the context"}
	return render_to_response('rango/index.html',context_dict,context)

def about(request):
	return HttpResponse("Rango says: Here is the about page. <a href=\"http://127.0.0.1:8000/rango/\">Back to Index</a>")