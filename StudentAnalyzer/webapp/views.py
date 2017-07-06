from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def webappindex(request):
	return HttpResponse("<h2>Hello Prudhvi!!<h2>")
