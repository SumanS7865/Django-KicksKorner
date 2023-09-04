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
    path("forgotpassword", views.forgotpassword, name="forgotpassword"),
    path("resetpassword", views.resetpassword, name="resetpassword"),
    path("activate/<uidb64>/<token>", views.activate, name="activate"),
    path(
        "resetpassword_validate/<uidb64>/<token>",
        views.resetpassword_validate,
        name="resetpassword_validate",
    ),
    path("my_orders/", views.my_orders, name="my_orders"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("change_password/", views.change_password, name="change_password"),
    path("order_detail/<int:order_id>/", views.order_detail, name="order_detail"),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
