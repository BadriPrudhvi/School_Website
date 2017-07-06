from django.shortcuts import render
from django.http import HttpResponse

def personalindex(request):
	return render(request,'personal/home.html')

