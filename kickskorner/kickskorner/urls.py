from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from kickskorner.settings import DEBUG


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('store/', include('app.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('members.urls')),
    path('', include('category.urls')),
]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

