from django.db import models
from django.conf import settings

class Lawyer(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="이름", null=True)
    email = models.CharField(max_length=50, verbose_name="이메일", null=True)
    title = models.CharField(max_length=40, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    company_address = models.CharField(max_length=128, verbose_name="회사주소")
    company_phone_number = models.IntegerField(verbose_name="회사전화번호")
    career = models.CharField(max_length=128, verbose_name="경력")
    qualification = models.TextField( verbose_name="자격")
    education = models.TextField(verbose_name="학력")
    activity = models.TextField(verbose_name="활동사항")
    img = models.ImageField(upload_to="lawyer_img", blank=True, null=True, verbose_name="변호사 이미지")

    def __str__(self):
        return self.title

    class Meta:
        db_table = '변호사찾기'
        verbose_name='변호사찾기'
        verbose_name_plural = '변호사찾기'


class Lawyer_comment(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="이름", null=True)
    content = models.TextField(verbose_name="후기내용")
    time_point = models.IntegerField()
    kindness_point = models.IntegerField()
    solution_point = models.IntegerField()
    created_date = models.DateTimeField(null=True, blank=True, verbose_name="후기작성일")

    def __str__(self):
        return self.content

    class Meta:
        db_table = '변호사찾기 댓글'
        verbose_name = '변호사찾기 댓글'
        verbose_name_plural = '변호사찾기 댓글'











