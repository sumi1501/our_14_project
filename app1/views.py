from django.shortcuts import render

# Create your views here.
def dog(request):
    return render(request,'dog.html')