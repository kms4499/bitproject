from django.contrib import admin
from .models import Tip

class TipAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'img',
        'video_key',
        'created_date',
    )
    search_fields = ['title', 'content', 'img', 'video_key', 'created_date']

admin.site.register(Tip, TipAdmin)