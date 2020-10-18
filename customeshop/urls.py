"""customeshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  path, re_path, include, reverse_lazy
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views

from catalogs.views import CatalogViewSet, ProductViewSet
from carts.views import OrderView, OrderItemView


router = DefaultRouter()
router.register(r'catalogs', CatalogViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderView)
router.register(r'items', OrderItemView, basename='OrderItem')


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include(router.urls)),
   
    path('api-auth/', include('rest_framework.urls')), 
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    re_path(r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
