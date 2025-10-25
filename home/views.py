from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index/index.html")
def signupas(request):
    return render(request,"index/signupas.html")
def loginas(request):
    return render(request,"index/loginas.html")
def contact(request):
    return render(request,"index/contact.html")
def about(request):
    return render(request,"index/about.html")
def details(request):
    return render(request,"index/details.html")