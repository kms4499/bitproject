from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Lawyer, Lawyer_comment
from .forms import LawyerForm, Lawyer_commentForm
from users.decorators import *
from django.contrib import messages


def index(request):
    lawyer_list = Lawyer.objects.all().order_by('-id')  # 최근생성시간 순으로
    page = request.GET.get('page', '1')
    paginator = Paginator(lawyer_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'lawyer_list':page_obj}
    return render(request, 'lawyer/lawyer_list.html', context)

# 일반인이랑 변호사 구별해야됨 데코레이터 사용
def detail(request, lawyer_id):
    lawyer = get_object_or_404(Lawyer, pk=lawyer_id)
    context = {'lawyer':lawyer}
    return render(request, 'lawyer/lawyer_detail.html', context)

def lawyer_create(request):
    if request.method == 'POST':
        form = LawyerForm(request.POST, request.FILES)
        if form.is_valid():
            lawyer = form.save(commit=False)
            lawyer.save()
            return redirect('lawyer:index')
    else:
        form = LawyerForm()
    context = {'form': form}
    return render(request, 'lawyer/lawyer_form.html', context)

def lawyer_modify(request, lawyer_id):
    lawyer = get_object_or_404(Lawyer, pk=lawyer_id)
    if request.user != lawyer.name:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('lawyer:detail', lawyer_id=lawyer.id)

    if request.method == 'POST':
        form = LawyerForm(request.POST, instance=lawyer)
        if form.is_valid():
            lawyer = form.save(commit=False)
            lawyer.name = request.user
            lawyer.save()
            return redirect('lawyer:detail', lawyer_id=lawyer.id)
    else:
        form = LawyerForm()
    context = {'form' : form}
    return render(request, 'lawyer/lawyer_form.html', context)

def lawyer_delete(request, lawyer_id):
    lawyer = get_object_or_404(Lawyer, pk=lawyer_id)
    if request.user != lawyer.name:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('lawyer/lawyer:detail', lawyer_id=lawyer.id)
    lawyer.delete()
    return redirect('lawyer:index')


# 댓글등록
def comment_create(request, lawyer_id):
    lawyer = get_object_or_404(Lawyer, pk=lawyer_id)
    if request.method == "POST":
        form = Lawyer_commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.title = lawyer
            comment.name = request.user
            comment.save()
            return redirect('lawyer:detail', lawyer_id=lawyer.id)
    else:
        form = Lawyer_commentForm()
    context = {'form': form}
    return render(request, 'lawyer/comment_form.html', context)

#댓글 수정
def comment_modify(request, comment_id):
    comment = get_object_or_404(Lawyer_comment, pk=comment_id)
    if request.user != comment.name:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('lawyer:detail', lawyer_id=comment.content.id)

    if request.method == "POST":
        form = Lawyer_commentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.name = request.user
            comment.save()
            return redirect('lawyer:detail', lawyer_id=comment.content.id)
    else:
        form = Lawyer_commentForm(instance=comment)
    context = {'form': form}
    return render(request, 'lawyer/comment_form.html', context)

#댓글삭제
def comment_delete(request, comment_id):
    comment = get_object_or_404(Lawyer_comment, pk=comment_id)
    if request.user != comment.name:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('lawyer:detail', lawyer_id=comment.content.id)
    else:
        comment.delete()
    return redirect('lawyer:detail', lawyer_id=comment.content.id)


