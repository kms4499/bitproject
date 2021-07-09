from django.shortcuts import render, redirect
from django import forms
from free.models import Free, Comment

class FreeForm(forms.ModelForm):
    class Meta:
        model = Free
        fields = ['title', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }

# class AnswerForm(forms.ModelForm):
#     class Meta:
#         model = Answer
#         fields = ['content']
#         labels = {
#             'content': '답변내용',
#         }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels= {
            'content' : '댓글내용',
        }