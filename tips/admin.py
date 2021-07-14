from django.contrib import admin
from .models import Tip

class TipAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'img',
        'url',
        'created_date',
    )
    search_fields = ['title', 'content', 'img', 'url', 'created_date']

admin.site.register(Tip, TipAdmin)