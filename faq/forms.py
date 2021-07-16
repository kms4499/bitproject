from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content','question_case']
        labels = {
            'title':'제목',
            'content':'내용',
            'question_case':'질문유형',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content','answer_case']
        labels = {
            'content':'내용',
            'answer_case':'답변유형',
        }