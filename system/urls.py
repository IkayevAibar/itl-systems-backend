from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from app.views import LeadViewSet, TextContentViewSet, ImageContentViewSet

from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('leads', LeadViewSet, basename='lead-list')
router.register('text-contents', TextContentViewSet, basename='text-content-list')
router.register('image-contents', ImageContentViewSet, basename='image-content-list')

urlpatterns = [
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




urlpatterns += router.urls