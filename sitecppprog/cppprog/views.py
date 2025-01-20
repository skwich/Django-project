from django.shortcuts import render
from django.core import serializers

from .models import *


def index(request):
    return render(request, 'cppprog/index.html')

def statistics(request):
    salary_dynamics_of_years = serializers.serialize("python", SalaryDynamicsOfYear.objects.all())
    count_dynamics_of_years = serializers.serialize("python", CountDynamicsOfYear.objects.all())
    salary_dynamics_of_city = serializers.serialize("python", SalaryDynamicsOfCity.objects.all())
    rate_of_city = serializers.serialize("python", RateOfCity.objects.all())
    top20_skills = serializers.serialize("python", Top20Skills.objects.all())
    years_of_top20 = list(set(Top20Skills.objects.all().values_list('year', flat=True)))
    years_of_top20.sort(reverse=True)

    context = {
        'salary_dynamics_of_years': salary_dynamics_of_years,
        'count_dynamics_of_years': count_dynamics_of_years,
        'salary_dynamics_of_city': salary_dynamics_of_city,
        'rate_of_city': rate_of_city,
        'top20_skills': top20_skills,
        'years_of_top20': years_of_top20
    }
    return render(request, 'cppprog/statistics.html', context=context)

def relevance(request):
    salary_dynamics_of_years = serializers.serialize("python", VacancySalaryDynamicsOfYear.objects.all())
    count_dynamics_of_years = serializers.serialize("python", VacancyCountDynamicsOfYear.objects.all())

    context = {
        'salary_dynamics_of_years': salary_dynamics_of_years,
        'count_dynamics_of_years': count_dynamics_of_years,
    }
    return render(request, 'cppprog/relevance.html', context=context)

def geography(request):
    salary_dynamics_of_city = serializers.serialize("python", VacancySalaryDynamicsOfCity.objects.all())
    rate_of_city = serializers.serialize("python", VacancyRateOfCity.objects.all())

    context = {
        'salary_dynamics_of_city': salary_dynamics_of_city,
        'rate_of_city': rate_of_city
    }
    return render(request, 'cppprog/geography.html', context=context)

def skills(request):
    top20_skills = serializers.serialize("python", VacancyTop20Skills.objects.all())
    years_of_top20 = list(set(VacancyTop20Skills.objects.all().values_list('year', flat=True)))
    years_of_top20.sort(reverse=True)

    context = {
        'top20_skills': top20_skills,
        'years_of_top20': years_of_top20
    }
    return render(request, 'cppprog/skills.html', context=context)

def last_vacs(request):
    return render(request, 'cppprog/last_vacs.html')