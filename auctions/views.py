from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Category, Listing, Bid


def index(request):
    """
    Display All active listings for ALL users (loggedin or not)
    """
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
     })

    # NEED (IN FUTURE) TO FILTER VIA 'IS_ACTIVE" FIELD 
    

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def my_listing(request, user_id):
    """
    Display All active listings for one logged in user only.
    """

    current_user = User.objects.get(pk=user_id)
    print(user_id)
    print("10:")
    print(current_user)
    filtered_listings = Listing.objects.filter(user_id=user_id)
    print("20:")
    print(filtered_listings)
    return render(request, "auctions/index.html", {
       "listings": filtered_listings
    })

    #WORKS 
    #NEED:
    # 1. MAKE changes on index.html. ++ ADD filter on "is_active"
    # 2. ADD link to not-active listings too for this User only


def listing(request, listing_id):
    """
    Display Individual Listing Page.
    """

    listing = Listing.objects.get(pk=listing_id)  
    return render(request, "auctions/listing.html", {
        "listing": listing
    })
#NEED Maybe: Error checking - Redirect to Page Is Not Found if a user try a listing that doesn't exist.