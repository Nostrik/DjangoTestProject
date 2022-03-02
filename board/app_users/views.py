from re import template
import time
import datetime
from multiprocessing import AuthenticationError
from django.shortcuts import render
from app_users.forms import AuthForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView


def login_view(request):
	if request.method == 'POST':  # для POST попытка аутентификации ползователя
		auth_form = AuthForm(request.POST)
		print(time.ctime())
		if auth_form.is_valid():
			username = auth_form.cleaned_data['username']
			password = auth_form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					if user.is_superuser == False:
						login(request, user)
						return HttpResponse('Вы успешно вошли в систему')
					else:
						auth_form.add_error('__all__', 'Администраторам доступ запрешен')
				else:
					auth_form.add_error('__all__', 'Ошибка Учетная запись не активна.')
			else:
				auth_form.add_error('__all__', 'Ошибка ввода.')

	else:  # для всех остальных запроссов, просто отображаем саму страничку логина
		auth_form = AuthForm()
	context = {
		'form': auth_form
	} 
	return render(request, 'users/login.html', context=context)


class AnotherLoginView(LoginView):
	template_name = 'users/login.html'


class AnotherLogoutView(LogoutView):
	# template_name = 'users/logout.html'
	next_page = '/'


def logout_view(request):
	logout(request)
	return HttpResponse('Вы успешно вышли из под своей своей учетной записи')
