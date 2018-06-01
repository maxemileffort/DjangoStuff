from django.shortcuts import render

# Create your views here.
def homeinfo(request):
    return render(request, 'homeinfo.html')
