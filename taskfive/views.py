from django.shortcuts import render

def index(request):
    return render(request, 'taskfive/task5.html')
