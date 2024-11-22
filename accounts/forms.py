# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['title', 'url', 'parent', 'order', 'image']
    
    # Add Bootstrap classes directly to each field
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter menu item title'}), required=True)
    url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL'}))
    order = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter order number'}))
    parent = forms.ModelChoiceField(queryset=MenuItem.objects.all(), required=False, empty_label="None", widget=forms.Select(attrs={'class': 'form-select'}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control','type' : 'file', 'id' : 'form-file'}), required=True)

    def clean_image(self):
        image = self.cleaned_data.get('image')
        
        # If an image is provided, ensure it's in PNG format
        if image:
            # Check if the image file name ends with '.png'
            if not image.name.lower().endswith('.png'):
                raise ValidationError("Only PNG images are allowed.")
            
            # Check the content type (MIME type) to be 'image/png'
            if image.content_type != 'image/png':
                raise ValidationError("Only PNG images are allowed.")
                        # Truncate the image filename to the first 3 words (using spaces to separate)
            file_name = image.name.split('.')[0]  # Get file name without extension
            words = file_name.split()  # Split the name by spaces (words)
            truncated_name = ' '.join(words[:3])  # Keep only the first 3 words
            # If you want to keep the extension, append it back
            truncated_name_with_extension = f"{truncated_name}.png"
            
            # Replace the image name with the truncated name
            image.name = truncated_name_with_extension

        
        return image


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['image', 'title', 'subtitle', 'description', 'button_text', 'button_link', 'select_section']

    # Assign Bootstrap classes to each field directly
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control','type' : 'file', 'id' : 'form-file'}), required=True)
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter slider title'}), required=True)
    subtitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subtitle'}), required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter slider description'}), required=True)
    button_text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Button text'}), required=True)
    button_link = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Button URL'}), required=False)
    
    # New field for section selection with Bootstrap class
    select_section = forms.ChoiceField(
        choices=Slider.SECTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),required=True
    )