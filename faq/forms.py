from django import forms
from faq.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_case','title', 'content']
        labels = {
            'title':'제목',
            'content':'내용',
            'question_case':'질문유형',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_case', 'content']
        labels = {
            'content':'내용',
            'answer_case':'답변유형',
        }