from django.shortcuts import render, redirect, get_object_or_404
from app.forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import login, update_session_auth_hash, logout, get_user_model
from app.models import *
from django.contrib.admin.views.decorators import staff_member_required

User = get_user_model()

def home(request):
    current_newsletter = Newsletter.objects.order_by('-id').first()
    return render(request, "home.html", {"newsletter": current_newsletter})

def behind_counter_view(request):
    return render(request, "behind_counter.html")

def community_view(request):
    reviews = Review.objects.order_by('-id')
    current_newsletter = Newsletter.objects.order_by('-id').first()

    context = {
        "newsletter": current_newsletter,
        "reviews": reviews
    }

    return render(request, "community/community.html", context)
def all_newsletter_view(request):
    all_newsletters = Newsletter.objects.all()
    paginator = Paginator(all_newsletters, 10)  
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, 'all_news.html', {"page_obj": page_obj})
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
            return redirect("owner_portal")
    else:
        form = CustomAuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")

def sign_up_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "sign_up.html", {"form": form})

def create_review_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.rating = request.POST.get("rating")     
            if post.rating == '':
                raise ValueError        
            post.save()
            return redirect('community_view')
    else:
        form = ReviewForm()
    
    return render(request, 'forms/create_review.html', {'form': form})


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
            return redirect("owner_portal")
    else:
        form = NewsForm()
    return render(request, "forms/news_form.html", {"form": form})

@login_required
def newsletter_list(request):
    all_newsletters = Newsletter.objects.all()
    paginator = Paginator(all_newsletters, 10)  
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, 'news_list.html', {"page_obj": page_obj})

@login_required
def news_update_form_view(request, id):
    news_item = get_object_or_404(Newsletter, id=id)

    if request.method == "POST":
        form = NewsForm(request.POST, instance=news_item)
        if form.is_valid():
            form.save()
            return redirect("owner_portal")
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
