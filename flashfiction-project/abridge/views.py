from django.shortcuts import render

# Create your views here.
def abridge(request):
    return render(request, 'abridge.html')