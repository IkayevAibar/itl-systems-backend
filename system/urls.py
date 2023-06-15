from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from app.views import LeadListCreateAPIView, LeadRetrieveAPIView, TextContentListCreateAPIView, TextContentRetrieveAPIView, ImageContentListCreateAPIView, ImageContentRetrieveAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path('leads/', LeadListCreateAPIView.as_view(), name='lead-list'),
    path('leads/<str:pk>/', LeadRetrieveAPIView.as_view(), name='lead-detail'),
    path('textcontents/', TextContentListCreateAPIView.as_view(), name='textcontent-list'),
    path('textcontents/<int:pk>/', TextContentRetrieveAPIView.as_view(), name='textcontent-detail'),
    path('imagecontents/', ImageContentListCreateAPIView.as_view(), name='imagecontent-list'),
    path('imagecontents/<int:pk>/', ImageContentRetrieveAPIView.as_view(), name='imagecontent-detail'),
]