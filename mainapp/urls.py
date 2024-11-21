from django.urls import path
from .views import *

urlpatterns = [
  path('main_index/', main_index,name='main-index'),
  path('main/', main,name='main'),
  path('try/', try4,name='try'),
]
