from django.shortcuts import render

from board.app_employment.models import Vacancy
from app_employment.models import Vacancy


def vacancy_list(request):
    if request.user.has_perm():
        vacancies = Vacancy.objects.all()
        return render(request, 'employment/vacancy_list.html', {'vacancy_list': vacancies})
