from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Anni Bhaiya'})

def add(request):
    if request.method == 'POST':
        val1 = int(request.POST.get("num1", 0))  # Default value of 0 if num1 is not provided
        val2 = int(request.POST.get("num2", 0))  # Default value of 0 if num2 is not provided
        res = val1 + val2
        return render(request, 'result.html', {'result': res})
    else:
        # Handle GET request if necessary
        return HttpResponse("Method not allowed")