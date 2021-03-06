from django.contrib import admin
from .models import Lawyer, Lawyer_comment

class LawyerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'title',
        'content',
        'company_address',
        'company_phone_number',
        'career',
        'qualification',
        'education',
        'activity',
        'img',
    )
    search_fields = ['name', 'email', 'title', 'content', 'company_address', 'company_phone_number',
                     'career', 'qualification', 'education', 'activity', 'img']

class Lawyer_commentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'content',
        'created_date',
    )
    search_fields = ['name', 'content', 'created_date']

admin.site.register(Lawyer, LawyerAdmin)
admin.site.register(Lawyer_comment, Lawyer_commentAdmin)