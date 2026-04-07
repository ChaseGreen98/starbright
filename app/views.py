from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import get_user_model
from app.models import *

User = get_user_model()

def menu_view(request):
    items = Menu_Item.objects.all()

    paginator = Paginator(items, 4)
    page_obj = paginator.get_page(request.GET.get("page"))

def merch_view(request):
    items = Merch_Item.objects.all()

    paginator = Paginator(items, 4)
    page_obj = paginator.get_page(request.GET.get("page"))
