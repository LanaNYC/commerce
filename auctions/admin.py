from django.contrib import admin
from .models import Bid, Category, Listing, User, Comment, Watchlist

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Watchlist)
admin.site.register(Comment)


