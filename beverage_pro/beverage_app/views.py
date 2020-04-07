from django.shortcuts import render
from beverage_app.models import *
#from models import *


# Create your views here.
from django.http import HttpResponse

#define a function 
#def index(request):
	#return HttpResponse(“welcome”)



def index(request):
	#return render(request,'index.html')
	all=Beverage.objects.all()
	#s = Books.objects.all()
	context = {"all_beverage":all,"name":"Sarmi"}
	return render(request,"index.html",context)
def add_beverage(request):
	if request.method == "POST":
		  beverage_obj = Beverage()
		  beverage_obj.beverage_title = request.POST["beverage_title"]
		  beverage_obj.beverage_description = request.POST["beverage_description"]
		  beverage_obj.save()
	return render(request,"add_beverage.html")