from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location', 'category', 'status', 'available_seats', 'capacity', 'price_per_person']
    list_filter = ['status', 'category', 'date']
    search_fields = ['title', 'location', 'description']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Informations de base', {
            'fields': ('title', 'description', 'category', 'status')
        }),
        ('Date et lieu', {
            'fields': ('date', 'location')
        }),
        ('Capacité et tarification', {
            'fields': ('capacity', 'available_seats', 'price_per_person')
        }),
        ('Média', {
            'fields': ('image_url',)
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
