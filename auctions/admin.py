from django.contrib import admin
from .models import User, Categories, Listings

# Register your models here.
admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Listings)


