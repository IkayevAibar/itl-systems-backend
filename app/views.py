from rest_framework import generics, filters, viewsets, status, mixins
from rest_framework.response import Response
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


class LeadViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_class = LeadFilter
    ordering_fields = ['created_at']
    search_fields = ['id','name', 'email', 'phone']


    

class TextContentViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = TextContent.objects.all()
    serializer_class = TextContentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_class = TextContentFilter
    ordering_fields = ['created_at']
    search_fields = ['id','key', 'content']


class ImageContentViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = ImageContent.objects.all()
    serializer_class = ImageContentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_class = ImageContentFilter
    ordering_fields = ['created_at']
    search_fields = ['id','key']
