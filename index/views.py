from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        
    return render(request, 'index.html')

def output(request):
    pass
