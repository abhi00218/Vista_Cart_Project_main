# views.py
from django.shortcuts import render,redirect
from accounts.models import MenuItem
from .models import *
from .forms import *
from accounts.models import *
from accounts.forms import *

def main_index(request):
    return render(request, 'index.html')


def main(request):
    menu_items = MenuItem.objects.all().order_by('order')
    sliders = Slider.objects.all()
    # sliders = Slider.objects.filter(select_section=1)
    print(sliders)
    return render(request, 'main.html', {'menu_items': menu_items,'sliders': sliders})

def try4(request):
    return render(request,'test.html')







