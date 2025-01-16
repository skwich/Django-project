from django.shortcuts import render


def index(request):
    return render(request, 'cppprog/index.html')

def statistics(request):
    return render(request, 'cppprog/statistics.html')

def relevance(request):
    return render(request, 'cppprog/relevance.html')

def geography(request):
    return render(request, 'cppprog/geography.html')

def skills(request):
    return render(request, 'cppprog/skills.html')

def last_vacs(request):
    return render(request, 'cppprog/last_vacs.html')