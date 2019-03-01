from django.shortcuts import render

def home(request):
    response = {'home':'active'}
    return render(request, "Main/home.html", response)
