from django.db import models

from django.conf import settings

class Question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자', null=True)
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    created_date = models.DateTimeField(null=True, blank=True, verbose_name='등록시간')
    modify_date = models.DateTimeField(null=True, blank=True, verbose_name='수정일시')
    question_case = models.CharField(max_length=24, verbose_name="질문유형", null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = '질문하기'
        verbose_name = '질문하기'
        verbose_name_plural = '질문하기'

class Answer(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='답변자', null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(null=True, blank=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    answer_case = models.CharField(max_length=24, verbose_name="대답유형", null=True)

    class Meta:
        db_table = '답변하기'
        verbose_name = '답변하기'
        verbose_name_plural = '답변하기'
