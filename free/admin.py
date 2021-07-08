from django.contrib import admin
from .models import Free, Comment

class FreeAdmin(admin.ModelAdmin):
    list_display = (
        'writer',
        'title',
        'content',
        'create_date',
    )
    search_fields = ['writer', 'title', 'content', 'create_date']

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'writer',
        'content',
        'create_date',
        'modify_date',
        'title',
    )
    search_fields = ['writer','content','create_date','modify_date','title']

admin.site.register(Free, FreeAdmin)
admin.site.register(Comment, CommentAdmin)