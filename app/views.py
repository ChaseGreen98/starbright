from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import get_user_model
from app.models import *

User = get_user_model()

def home(request):
    return render(request, "home.html")

def behind_counter_view(request):
    return render(request, "behind_counter.html")

def community_view(request):
    return render(request, "community.html")

def menu_view(request):
    items = Menu_Item.objects.all()

    paginator = Paginator(items, 4)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, "menu.html", {"page_obj": page_obj})
    # ^^ i dont know enough about pagination to know what else to add here but i would assume something needs to be added

def merch_view(request):
    items = Merch_Item.objects.all()

    paginator = Paginator(items, 4)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, "merch.html", {"page_obj": page_obj})
    # ^^ and also here
