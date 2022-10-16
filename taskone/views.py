from django.shortcuts import render

def index(request):
    return render(request, 'taskone/task1.html')
