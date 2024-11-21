from .models import MenuItem
from .forms import MenuItemForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import SignUpForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib import messages

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('login')  # Redirect to login page after signup
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # User is authenticated, login and redirect to admin_index
            user = form.get_user()
            login(request, user)
            return redirect('admin-index')  # Redirect to the admin index page
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})



def admin_index_view(request):
    return render(request, 'accounts/Admin_index.html')

def user_admin(request):
    menu_items = MenuItem.objects.filter(parent=None)
    sliders = Slider.objects.all()
    menu_item_class_name = MenuItem.__name__  # Class name for MenuItem
    slider_class_name = Slider.__name__  # Class name for Slider
    
    # Pass the menu_items, sliders, and model class names to the template
    return render(request, 'accounts/user_admin.html', {
        'menu_items': menu_items,
        'sliders': sliders,
        'menu_item_class_name': menu_item_class_name,
        'slider_class_name': slider_class_name,
    })




def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)  # Handle POST request with files

        if form.is_valid():
            menu_item = form.save()  # Save the form, including the image
            return redirect('add-menu-item')  # Redirect to the list page after saving the menu item
    else:
        form = MenuItemForm()

    return render(request, 'accounts/add_menu_item.html', {'form': form})








def edit_menu_item(request, item_id):
    # Fetch the menu item to edit
    item = get_object_or_404(MenuItem, id=item_id)
    
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('menu-view')  # Redirect to the menu list after editing
    else:
        form = MenuItemForm(instance=item)
    
    return render(request, 'accounts/edit_menu_item.html', {'form': form, 'item': item})


def delete_menu_item(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    item.delete()
    return redirect('menu-view')  # Redirect to the menu list after deletion



def edit_slider(request, id):
    slider = get_object_or_404(Slider, id=id)
    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES, instance=slider)
        if form.is_valid():
            form.save()
            messages.success(request, 'Slider updated successfully!')
            return redirect('menu-view')
    else:
        form = SliderForm(instance=slider)
    return render(request, 'accounts/edit_slider.html', {'form': form})

def delete_slider_item(request, id):
    slider = get_object_or_404(Slider, id=id)
    slider.delete()
    messages.success(request, 'Slider deleted successfully!')
    return redirect('slider-view')

def menu_view(request):
    menu_items = MenuItem.objects.filter(parent=None)
    return render(request, 'accounts/menu_view.html',{'menu_items': menu_items})

def slider_view(request):
    sliders = Slider.objects.all()
    return render(request, 'accounts/slider_view.html',{'sliders': sliders})

def add_slider(request):
    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the new slider entry to the database
            return redirect('add-slider')  # Redirect to the page where the slider is displayed
    else:
        form = SliderForm()
    
    return render(request, 'accounts/add_slider.html', {'form': form})



