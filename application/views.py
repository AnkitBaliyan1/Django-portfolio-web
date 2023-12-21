from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'mywebsite/home.html')

def about(request):
    return render(request, "mywebsite/about.html")

def academics(request):
    return render(request, "mywebsite/academics.html")

def machinelearning(request):
    return render(request, "mywebsite/machinelearning.html")

def sql(request):
    return render(request, "mywebsite/sql.html")

def bitools(request):
    return render(request, "mywebsite/bitools.html")

def llm(request):
    return render(request, "mywebsite/llm.html")

def upcoming(request):
    return render(request, "mywebsite/upcoming.html")