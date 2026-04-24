from django.shortcuts import render, redirect, get_object_or_404
from app.forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import login, update_session_auth_hash, logout, get_user_model
from app.models import *

User = get_user_model()

def home(request):
    current_newsletter = Newsletter.objects.order_by('-id').first()
    return render(request, "home.html", {"newsletter": current_newsletter})

def behind_counter_view(request):
    return render(request, "behind_counter.html")

def community_view(request):
    current_newsletter = Newsletter.objects.order_by('-id').first()
    return render(request, "community/community.html", {"newsletter": current_newsletter})

# ^^^
# i kinda want to add another page or just a collapsable section for users to be able to see old newsletters,
# like maybe the last 3 - 5 posted newsletters.
# definitely not all of them though because at some point that's gonna be a lot of newsletters. 
# OR OR OR CHASE YOU COULD WORK YOUR FANCY PAGINATION MAGIC !!!


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("owner_portal_view")
    else:
        form = CustomAuthenticationForm()
    return render(request, "login.html", {"form": form})

@login_required
def owner_portal_view(request):
    return render(request, "owner-files/owner_portal.html")

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
    return render(request, "forms/news_form.html", {"form": form})

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

    return render(request, "forms/newsletter_update_form.html", {"form": form})

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
    return render(request, "forms/password_update.html", {"form": form})