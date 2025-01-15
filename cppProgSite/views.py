from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def statistics(request):
    return render(request, 'statistics.html')

def relevance(request):
    return render(request, 'relevance.html')

def geography(request):
    return render(request, 'geography.html')

def skills(request):
    return render(request, 'skills.html')

def last_vacs(request):
    return render(request, 'last_vacs.html')

