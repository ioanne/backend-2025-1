from django.contrib import admin

from apps.career.models import Career


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    """
    Admin view for the Career model.
    """
    list_display = ('name', 'description', 'duration', 'created_at')
    search_fields = ('name',)
    list_filter = ('duration',)
    ordering = ('-created_at',)