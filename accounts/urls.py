# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('index/admin/', views.admin_index_view, name='admin-index'),
    path('add_menu_item/', views.add_menu_item, name='add-menu-item'),
    path('menu_view/', views.menu_view, name='menu-view'),
    path('slider_view/', views.slider_view, name='slider-view'),
    path('user/admin', views.user_admin, name='user-admin'),
    path('menu/edit/<int:item_id>/', views.edit_menu_item, name='edit-menu-item'),
    path('menu/delete/<int:item_id>/', views.delete_menu_item, name='delete-menu-item'),
    path('edit_slider/<int:id>/', views.edit_slider, name='edit-slider'),
    path('delete_slider/<int:id>/', views.delete_slider_item, name='delete-slider'),
    path('add_slider/', views.add_slider, name='add-slider'),


]


