from unicodedata import name
from django.urls import path
from app_users.views import login_view,logout_view,  AnotherLoginView, AnotherLogoutView
from django.urls import include

urlpatterns = [
	path('login/', login_view, name='login'),
	path('logout/', logout_view, name='logout'),
	path('another_login/', AnotherLoginView.as_view(), name='another_login'), 
	path('another_logout/', AnotherLogoutView.as_view(), name='another_logout')
]
