from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=500, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    order = models.IntegerField(default=0,blank=True)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        # Prevent the image from being deleted
        if self.image:
            # Optionally, you can save the image path for further processing
            image_path = self.image.path
            super().delete(*args, **kwargs)  # Delete the model instance itself
            # The image file will not be deleted here.
            return image_path
        else:
            super().delete(*args, **kwargs)

    class Meta:
        ordering = ['order']

class Slider(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    button_text = models.CharField(max_length=100,blank=True)
    button_link = models.URLField(blank=True, null=True)
    
    # New field for section selection
    SECTION_CHOICES = [
        ('1', 'Banner section 1'),
        ('2', 'Banner section 2'),
        ('3', 'Banner section 3'),
        ('4', 'Banner section 4'),
    ]
    
    select_section = models.CharField(
        max_length=20,
        choices=SECTION_CHOICES,
        default='home',  # Set a default value if required
    )

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        # Prevent the image from being deleted
        if self.image:
            # Optionally, you can save the image path for further processing
            image_path = self.image.path
            super().delete(*args, **kwargs)  # Delete the model instance itself
            # The image file will not be deleted here.
            return image_path
        else:
            super().delete(*args, **kwargs)



