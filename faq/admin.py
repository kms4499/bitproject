from django.contrib import admin
from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('author',
                    'title',
                    'content',
                    'created_date',
                    'modify_date',
                    'question_case',
                    )

    search_fields = ['author', 'title', 'content', 'created_date', 'modify_case']

class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'question',
        'content',
        'create_date',
        'modify_date',
        'answer_case',
    )
    search_fields = ['author', 'question', 'content', 'created_date', 'modify_date', 'answer_case']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)