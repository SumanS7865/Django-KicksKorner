from django.urls import path
from .import views
from kickskorner.settings import DEBUG, STATIC_URL, STATIC_ROOT, STATICFILES_DIRS, MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
from django.conf import settings


urlpatterns= [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.category_page, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('error', views.error, name="error"),


]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)