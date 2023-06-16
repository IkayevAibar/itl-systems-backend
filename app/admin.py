from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import SimpleUser, Lead, TextContent, ImageContent

class SimpleUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)

class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'args')
    search_fields = ('name', 'email', 'phone', 'args')
    # ordering = ('created_at',)

class TextContentAdmin(admin.ModelAdmin):
    list_display = ('key', 'content')
    search_fields = ('key', 'content')
    ordering = ('id',)

class ImageContentAdmin(admin.ModelAdmin):
    list_display = ('key', 'content')
    search_fields = ('key',)
    ordering = ('id',)

admin.site.register(SimpleUser, SimpleUserAdmin)
admin.site.register(Lead, LeadAdmin)
admin.site.register(TextContent, TextContentAdmin)
admin.site.register(ImageContent, ImageContentAdmin)