from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("Congrats, You did it FUCKER!!!")

