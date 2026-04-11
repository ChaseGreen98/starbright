from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("behind-the-counter/", behind_counter_view, name="behind_counter_view"),
    path("community/", community_view, name="community_view"),
    path("menu/", menu_view, name="menu_view"),
    path("login/", login_view, name="login_view" ),
    path("merch-update/", merch_update_form_view, name="merch_form"),
    path("merch-create/", merch_create_form_view, name="merch_update"),
    path("menu-update/", menu_update_form_view, name="menu_update"),
    path("menu-create/", menu_create_form_view, name="menu_form"),
]