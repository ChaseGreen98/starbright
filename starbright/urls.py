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
    path("login/", login_view, name="login_view" ),
    path("owner-portal/", owner_portal_view, name="owner_portal"),
    path("owner-portal/create-post/", news_create_form_view, name="create_post_view"),
    path("owner-portal/update-post/", news_update_form_view, name="update_post_view"),
    path("create-review/", create_review_view, name="create_review"),
    path("sign-up/", sign_up_view, name="sign_up"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)