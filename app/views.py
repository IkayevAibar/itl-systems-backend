from rest_framework import filters, viewsets, status, mixins, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from django_filters.rest_framework import DjangoFilterBackend, DateFilter
import django_filters

from .models import Lead, TextContent, ImageContent
from .serializers import LeadSerializer, TextContentSerializer, ImageContentSerializer
from django import forms
from django_filters import Filter

class DateFilter(Filter):
    field_class = forms.DateField

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('lookup_expr', 'date')
        super().__init__(*args, **kwargs)

    def filter(self, qs, value):
        if value:
            return qs.filter(**{'{}__{}'.format(self.field_name, self.lookup_expr): value})
        return qs

class LeadFilter(django_filters.FilterSet):
    created_at = DateFilter()
    created_at_range = django_filters.DateTimeFromToRangeFilter(field_name='created_at')

    class Meta:
        model = Lead
        fields = ['created_at', 'created_at_range']

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
    search_fields = ['name', 'email', 'phone']
    
    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    

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
    permission_classes = [permissions.IsAuthenticated]


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
    permission_classes = [permissions.IsAuthenticated]