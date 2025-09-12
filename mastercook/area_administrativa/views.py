from django.shortcuts import render, get_object_or_404


# Create your views here.

def adm(request):
    return render(request, 'administrativo.html')
