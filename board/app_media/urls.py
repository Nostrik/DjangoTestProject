from django.urls import path
from .views import *


urlpatterns = [
    path('upload_file/', upload_file, name='upload_file'),
    path('up_valid/', upload_valid_file, name='up_valid')
]