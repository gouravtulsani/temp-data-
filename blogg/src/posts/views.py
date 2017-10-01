from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def post_create(request):
	a = {"content" : "post_create"}
	return render(request, "index.html", a)



def post_detail(request):
	a = {"content" : "post_detail"}
	return render(request, "index.html", a)


	
def post_list(request):
	a = {"content" : "post_list"}
	return render(request, "index.html", a)


	
def post_update(request):
	a = {"content" : "post_update"}
	return render(request, "index.html", a)


	
def post_delete(request):
	a = {"content" : "post_delete"}
	return render(request, "index.html", a)


	