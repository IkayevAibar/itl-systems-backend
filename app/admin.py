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
    list_display = ('id', 'name', 'email', 'phone', 'args')
    search_fields = ('id', 'name', 'email', 'phone', 'args')
    ordering = ('id', 'name',)


admin.site.register(SimpleUser, SimpleUserAdmin)
admin.site.register(Lead, LeadAdmin)
admin.site.register(TextContent)
admin.site.register(ImageContent)