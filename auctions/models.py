from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self):
        return f"{self.username}"

class Category(models.Model):
    description = models.CharField(max_length=150)
    
    def __str__(self):
        return f" {self.description}"

class Listing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="listings") 
    title = models.CharField(max_length=64)
    description = models.TextField(blank = True)
    starting_bid = models.DecimalField(max_digits=8, decimal_places=2) #Maybe need to change it to allow Billion
    image = models.URLField(blank = True)
    category = models.ForeignKey(Category, null = True, blank=True, on_delete=models.CASCADE, related_name="categories")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}: {self.title} created by {self.user_id}"

class Bid(models.Model):
    ammount = models.DecimalField(max_digits=19, decimal_places=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userBids") 
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="allListingBids") 
    bidTime = models.DateTimeField()
    winning = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ammount} by {self.user} {self.bidTime}"

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="watchedListings")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE) #May need to add related_name

    def __str__(self):
        return f"{self.user} is watching {self.listing}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="comments")  
    commemtText = models.TextField(blank = True)

    def __str__(self):
        return f"{self.commentText} by {self.user}"    





