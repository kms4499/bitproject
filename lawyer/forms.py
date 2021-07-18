from django.shortcuts import render, redirect
from django import forms
from .models import Lawyer, Lawyer_comment

class LawyerForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        fields = ['img', 'email', 'title', 'content', 'company_name', 'company_address', 'company_phone_number',
                  'career', 'qualification', 'education', 'activity']
        labels = {
            'img' : '사진',
            'email' : '이메일',
            'title' : '제목',
            'content' : '내용',
            'company_name': '회사이름',
            'company_address' : '회사주소',
            'company_phone_number' : '회사전화번호',
            'career' : '경력내용',
            'qualification' : '자격',
            'education' : '학력',
            'activity' : '활동사항',
        }

class Lawyer_commentForm(forms.ModelForm):
    class Meta:
        model = Lawyer_comment
        fields = ['content']
        labels= {
            'content' : '리뷰내용',
        }