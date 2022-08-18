from django.db import models
from django.conf import settings

class Recipe(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='author', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    directions = models.TextField()
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    @property
    def get_image(self):
        if not self.image:
            return 'media/uploads/placeholder-image.png'
        return self.image.url


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




    