from django import forms
from .models import *



class NavigationItemForm(forms.ModelForm):
    class Meta:
        model = NavigationItem
        fields = ['title']


from django import forms










