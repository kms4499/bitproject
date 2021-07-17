from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Lawyer, Lawyer_comment
from users.decorators import *

def index(request):
    lawyer_list = Lawyer.objects.all().order_by('create_date')  # 최근생성시간 순으로
    page=request.GET.get('page', '1')
    paginator = Paginator(lawyer_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'lawyer_list':page_obj}
    return render(request, 'lawyer/lawyer_list.html', context)

# 일반인이랑 변호사 구별해야됨 데코레이터 사용
def detail(request, lawyer_id):
    lawyer = get_object_or_404(Lawyer, pk=lawyer_id)
    context = {'lawyer':lawyer}
    return render(request, 'lawyer/lawyer_detail_read.html', context)
