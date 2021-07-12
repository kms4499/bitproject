from django.db import models
from django.conf import settings
import os

class Free(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자', null=True)
    title = models.CharField(max_length=128,verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    create_date = models.DateTimeField(null=True, blank=True, verbose_name='등록시간')
    modify_date = models.DateTimeField(null=True, blank=True, verbose_name='글수정일시')
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = '자유게시판'
        verbose_name = '자유게시판'
        verbose_name_plural = '자유게시판'


class Comment(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='댓글작성자', null=True)
    title = models.ForeignKey(Free, null=True, blank=True, on_delete=models.CASCADE, verbose_name='이 댓글이 달린 게시글')
    content = models.TextField(verbose_name='댓글내용')
    create_date = models.DateTimeField(null=True, blank=True, verbose_name='댓글작성일시')
    modify_date = models.DateTimeField(null=True, blank=True, verbose_name='댓글수정일시')
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)

    def __str__(self):
        return self.content

    class Meta:
        db_table = '자유게시판 댓글'
        verbose_name = '자유게시판 댓글'
        verbose_name_plural = '자유게시판 댓글'




