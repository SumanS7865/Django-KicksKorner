from django.urls import path
from . import views
from kickskorner.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("user_dashboard/", views.user_dashboard, name="user_dashboard"),
    path("", views.user_dashboard, name="user_dashboard"),
    path("activate/<uidb64>/<token>", views.activate, name="activate"),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
