from rest_framework import generics, filters
from .models import Lead, TextContent, ImageContent
from .serializers import LeadSerializer, TextContentSerializer, ImageContentSerializer
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

class LeadFilter(django_filters.FilterSet):
    created_at = django_filters.DateTimeFromToRangeFilter(field_name='created_at')

    class Meta:
        model = Lead
        fields = ['created_at']

class TextContentFilter(django_filters.FilterSet):
    created_at = django_filters.DateTimeFromToRangeFilter(field_name='created_at')

    class Meta:
        model = TextContent
        fields = ['created_at']

class ImageContentFilter(django_filters.FilterSet):
    created_at = django_filters.DateTimeFromToRangeFilter(field_name='created_at')

    class Meta:
        model = ImageContent
        fields = ['created_at']


class LeadListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_class = LeadFilter
    ordering_fields = ['created_at']
    search_fields = ['id','name', 'email', 'phone']

class LeadRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class TextContentListCreateAPIView(generics.ListCreateAPIView):
    queryset = TextContent.objects.all()
    serializer_class = TextContentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_class = TextContentFilter
    ordering_fields = ['created_at']
    search_fields = ['id','key', 'content']

class TextContentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = TextContent.objects.all()
    serializer_class = TextContentSerializer

class ImageContentListCreateAPIView(generics.ListCreateAPIView):
    queryset = ImageContent.objects.all()
    serializer_class = ImageContentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_class = ImageContentFilter
    ordering_fields = ['created_at']
    search_fields = ['id','key']

class ImageContentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = ImageContent.objects.all()
    serializer_class = ImageContentSerializer