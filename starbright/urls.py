from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("behind-the-counter/", behind_counter_view, name="behind_counter_view"),
    path("community/", community_view, name="community_view"),
    
    path("menu/", menu_view, name="menu_view"),
    path("menu/coffee/", coffee_view, name="coffee_view"),
    path("menu/frappe/", frappe_view, name="frappe_view"),
    path("menu/kids/", kids_view, name="kids_view"),
    path("menu/food/", food_view, name="food_view"),
    path("menu/specialty/", specialty_view, name="specialty_view"),
    path("menu/lotus/", lotus_view, name="lotus_view"),
    path("menu/other/", other_view, name="other_view"),

    path("merch/", merch_view, name="merch_view"),
    path("login/", login_view, name="login_view" ),
    path("owner-portal/", owner_portal_view, name="owner_portal_view"),
    path("merch-update/<int:id>/", merch_update_form_view, name="merch_update"),
    path("merch-create/", merch_create_form_view, name="merch_form"),
    path("menu-update/<int:id>/", menu_update_form_view, name="menu_update"),
    path("menu-create/", menu_create_form_view, name="menu_form"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)