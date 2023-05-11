from django.urls import path
from .import views
from kickskorner.settings import DEBUG, STATIC_URL, STATIC_ROOT, STATICFILES_DIRS, MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('login', views.loginpage, name='loginform'),
    path('register', views.signuppage, name='signupform'),


    


]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)