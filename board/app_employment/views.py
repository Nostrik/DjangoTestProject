from django.shortcuts import render
# from board.app_employment.models import Vacancy
# from app_employment.models import Vacancy
from .models import Vacancy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required


@permission_required('app_employment.view_vacancy')
def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy_list.html', {'vacancy_list': vacancies})
