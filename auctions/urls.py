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

]
