from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:user_id>", views.my_listing, name="my_listing"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("listing/<int:listing_id>/add_watchlist", views.add_watchlist, name="add_watchlist"),
    path("listing/<int:listing_id>/remove_watchlist", views.remove_watchlist, name="remove_watchlist"),
    path("watchlist/<int:user_id>", views.watchlist, name="watchlist"),
    path("create/<int:user_id>", views.create_listing, name="create_listing"),
    path("listing/<int:listing_id>/place_bid", views.place_bid, name="place_bid"),
    path("listing/<int:listing_id>/close_listing", views.close_listing, name="close_listing"),
    path("closed_listing/<int:user_id>", views.closed_listing, name="closed_listing"),
    path("listing/<int:listing_id>/add_comment", views.add_comment, name="add_comment"),
    path("categories", views.all_categories, name="all_categories"),
    path("categories/<int:category_id>", views.display_category, name="display_category"),



]
