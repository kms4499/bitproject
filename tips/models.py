from django.db import models
from django.urls import reverse

class Tip(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    img = models.ImageField(upload_to="tips_img", blank=True, null=True,verbose_name='이미지')
    created_date = models.DateTimeField(null=True, blank=True, verbose_name='작성일')
    url = models.URLField('URL', null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = '법률팁'
        verbose_name = '법률팁'
        verbose_name_plural = '법률팁'

    def get_absolute_url(self):
        return reverse('tips:tips_detail', args=(self.title,))
