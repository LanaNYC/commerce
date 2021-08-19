from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self):
        return f"{self.id}: {self.username}"

class Categories(models.Model):
    description = models.CharField(max_length=150)
    
    def __str__(self):
        return f" {self.description}"

class Listings(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #May need to add related_name
    title = models.CharField(max_length=64)
    description = models.TextField(blank = True)
    starting_bid = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.URLField(blank = True)
    category = models.ForeignKey(Categories, null = True, blank=True, on_delete=models.CASCADE, related_name="categories")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}: {self.title} created by {self.user_id}"



