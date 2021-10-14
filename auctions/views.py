"""
items for 'auction' are from
https://harrypotter.fandom.com/wiki/
"""

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from django.forms import ModelForm

from .models import User, Category, Listing, Bid, Comment, Watchlist


# Create the form class.
class newListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'starting_bid', 'image', 'category', 'is_active']


def index(request):
    """
    Display All active listings for ALL users (loggedin or not)
    """
    listings = Listing.objects.filter(is_active = True)
    return render(request, "auctions/index.html", {
        "listings": listings
    })

    
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
    filtered_listings = Listing.objects.filter(user_id=user_id)
    return render(request, "auctions/index.html", {
       "listings": filtered_listings
    })

    #WORKS 
    #NEED:
    # 2. ADD link to not-active listings too for this User only
   

def listing(request, listing_id):
    """
    Display Individual Listing Page.
    """

    listing = Listing.objects.get(pk=listing_id)  
    item = Watchlist.objects.filter(listing=listing_id, user=request.user)
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "item": item
    })
#NEED 
# 1. Maybe: Error checking - Redirect to Page Is Not Found if a user try a listing that doesn't exist.
# 2. add "short_desription" to see on a page. ("Full description should be on Lisiting page")

def not_active_listing(request):
    pass
#TODO (MAYBE)


@login_required
def add_watchlist(request, listing_id):
    """
    Add a listing to a Watchlist
    """
    if request.method == "POST":
        listing = Listing.objects.get(pk=listing_id)
        if request.user.is_authenticated:
            user = request.user 
            new_watched_listing = Watchlist()
            new_watched_listing.user = request.user
            new_watched_listing.listing = listing
            new_watched_listing.save()
            return render(request, "auctions/listing.html", {
            "listing": listing,
            "message": "This auction was added to your watchlist."
            })
        else:
            return render(request, "auctions/login.html", {
                "message": "Please log in."
            })


@login_required
def remove_watchlist(request, listing_id):
    """
    Remove a listing to a Watchlist
    """
    if request.method == "POST":
        listing = Listing.objects.get(pk=listing_id)
        if request.user.is_authenticated:
            user = request.user 
            watched_listing = Watchlist.objects.filter(listing=listing_id, user=request.user)
            watched_listing.delete()
            return render(request, "auctions/listing.html", {
            "listing": listing,
            "message": "This auction was removed from your watchlist."
            })
        else:
            return render(request, "auctions/login.html", {
                "message": "Please log in."
            })
   

@login_required
def watchlist(request, user_id):
    """
    Display all of the listings that a user has added to their watchlist. 
    """
    current_user = User.objects.get(pk=user_id)
    filtered_watchlist = Watchlist.objects.filter(user_id=user_id)
    return render(request, "auctions/watchlist.html", {
       "watchlist": filtered_watchlist,
       "user": current_user
    })


@login_required
def create_listing(request, user_id):
 #STOPPEd HERE. NEED TO ADD FUNCTION TO EVOID SAVING THE SAME AUCTION

    if request.method == "POST":
        form = newListingForm(request.POST)
        if form.is_valid():
            #if form.title is None:
            new_action=form.save()
            return HttpResponseRedirect(reverse("index"))
            #else:   
                #return render(request, "auctions/create.html", {
                #"form": newListingForm(),
               # "message": "You already have an auction with this title."
                # })   
        else:
            return render(request, "auctions/create.html", {
                "form": newListingForm(),
                "message": "Your form is invalid."
            })   
    # If the method is GET, User will see an empty form
    else:
        return render(request, "auctions/create.html", {
            "form": newListingForm()
        })



#They should be able to specify a title for the listing, 
# a text-based description, and what the starting bid should be. 
# Users should also optionally be able to provide a URL for an image for the listing
#  and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).