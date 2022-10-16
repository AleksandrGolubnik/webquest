from django.shortcuts import render

def index(request):
    return render(request, 'tasktwo/task2.html')
