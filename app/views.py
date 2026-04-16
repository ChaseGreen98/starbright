from django.shortcuts import render, redirect, get_object_or_404
from app.forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import login, update_session_auth_hash, logout, get_user_model
from app.models import *

User = get_user_model()

def home(request):
    return render(request, "home.html")

def behind_counter_view(request):
    return render(request, "behind_counter.html")

def community_view(request):
    current_newsletter = Newsletter.objects.order_by('-id').first()
    return render(request, "community.html", {"newsletter": current_newsletter})

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("owner_portal_view")
    else:
        form = CustomAuthenticationForm()
    return render(request, "login.html", {"form": form})

def menu_view(request):
    # ^^ i might want to change this to work with the new category field i've added to the model, or something idk
    cof_items = Menu_Item.objects.filter(category='COF')
    fra_items = Menu_Item.objects.filter(category='FRA')
    kid_items = Menu_Item.objects.filter(category='KID')
    foo_items = Menu_Item.objects.filter(category='FOO')
    spe_items = Menu_Item.objects.filter(category='SPE')
    lot_items = Menu_Item.objects.filter(category='LOT')
    oth_items = Menu_Item.objects.filter(category='OTH')

    cof_paginator = Paginator(cof_items, 10)
    fra_paginator = Paginator(fra_items, 10)
    kid_paginator = Paginator(kid_items, 10)
    foo_paginator = Paginator(foo_items, 10)
    spe_paginator = Paginator(spe_items, 10)
    lot_paginator = Paginator(lot_items, 10)
    oth_paginator = Paginator(oth_items, 10)
    # TEMPORARY CHANGE PLEASE CHANGE IT BACK TO 10 BEFORE YOU PUSH MEGAN OH MY GOD
    cof_page_obj = cof_paginator.get_page(request.GET.get("page"))
    fra_page_obj = fra_paginator.get_page(request.GET.get("page"))
    kid_page_obj = kid_paginator.get_page(request.GET.get("page"))
    foo_page_obj = foo_paginator.get_page(request.GET.get("page"))
    spe_page_obj = spe_paginator.get_page(request.GET.get("page"))
    lot_page_obj = lot_paginator.get_page(request.GET.get("page"))
    oth_page_obj = oth_paginator.get_page(request.GET.get("page"))

    context = {
        "cof_page_obj": cof_page_obj,
        "fra_page_obj": fra_page_obj,
        "kid_page_obj": kid_page_obj,
        "foo_page_obj": foo_page_obj,
        "spe_page_obj": spe_page_obj,
        "lot_page_obj": lot_page_obj,
        "oth_page_obj": oth_page_obj,
    }

    return render(request, "menu.html", context)

def merch_view(request):
    items = Merch_Item.objects.all()

    paginator = Paginator(items, 10)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, "merch.html", {"page_obj": page_obj})

@login_required
def owner_portal_view(request):
    return render(request, "owner_portal.html")

@login_required
def owner_menu_view(request):
    items = Menu_Item.objects.all()

    paginator = Paginator(items, 10)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, "owner_menu.html", {"page_obj": page_obj})

@login_required
def owner_merch_view(request):
    items = Merch_Item.objects.all()

    paginator = Paginator(items, 10)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, "owner_merch.html", {"page_obj": page_obj})

@login_required
def menu_create_form_view(request):
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.save()
            return redirect("owner_portal_view")
    else:
        form = MenuForm()
    return render(request, "menu_form.html", {"form": form})

@login_required
def menu_update_form_view(request, id):
    menu_item = get_object_or_404(Menu_Item, id=id)

    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect("owner_portal_view")
    else:
        form = MenuForm(instance=menu_item)

    return render(request, "menu_item_update.html", {"form": form})

@login_required
def merch_create_form_view(request):
    if request.method == "POST":
        form = MerchForm(request.POST, request.FILES)
        if form.is_valid():
            merch_item = form.save(commit=False)
            merch_item.save()
            return redirect("owner_portal_view")
    else:
        form = MerchForm()
    return render(request, "merch_form.html", {"form": form})

@login_required
def merch_update_form_view(request, id):
    merch_item = get_object_or_404(Merch_Item, id=id)

    if request.method == "POST":
        form = MerchForm(request.POST, request.FILES, instance=merch_item)
        if form.is_valid():
            form.save()
            return redirect("owner_portal_view")
    else:
        form = MerchForm(instance=merch_item)

    return render(request, "merch_item_update.html", {"form": form})

@login_required
def news_create_form_view(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news_item = form.save(commit=False)
            news_item.save()
            return redirect("owner_portal_view")
    else:
        form = NewsForm()
    return render(request, "news_form.html", {"form": form})

@login_required
def news_update_form_view(request, id):
    news_item = get_object_or_404(Newsletter, id=id)

    if request.method == "POST":
        form = NewsForm(request.POST, instance=news_item)
        if form.is_valid():
            form.save()
            return redirect("owner_portal_view")
    else:
        form = NewsForm(instance=news_item)

    return render(request, "newsletter_update_form.html", {"form": form})

@login_required
def password_change_view(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect("owner_portal_view")
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, "password_update.html", {"form": form})