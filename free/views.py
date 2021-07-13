from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone
from .forms import FreeForm, CommentForm
from .models import Free, Comment
from django.core.paginator import Paginator
from users.decorators import *

# def post_new(request):
#
#     if request.method == 'POST':
#         form = FreeForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.save()
#         return redirect('free/free_list.html')
#     else:
#         form = FreeForm()
#     return render(request, 'free/free_form.html', {
#         'form': form
#     })

def index(request):
    free_list = Free.objects.all().order_by('create_date') # 최근생성시간 순으로
    page = request.GET.get('page', '1')  # 페이지
    paginator = Paginator(free_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'free_list': page_obj}
    return render(request, 'free/free_list.html', context)

def detail(request, free_id):
    free = get_object_or_404(Free, pk=free_id)
    context = {'free': free}
    return render(request, 'free/free_detail.html', context)


def free_create(request):
    if request.method == 'POST':
        form = FreeForm(request.POST)
        if form.is_valid():
            free = form.save(commit=False)
            free.create_date = timezone.now()
            free.save()
            return redirect('free:index')
    else:
        form = FreeForm()
    context = {'form': form}
    return render(request, 'free/free_form.html', context)

# @login_required(login_url='common:login'), 질문수정
def free_modify(request, free_id):
    free = get_object_or_404(Free, pk=free_id)
    if request.user != free.writer:
        messages.error(request, '수정권한이 없습니다')
        return redirect('free:detail', free_id=free.id)

    if request.method == "POST":
        form = FreeForm(request.POST, instance=free)
        if form.is_valid():
            free = form.save(commit=False)
            free.writer = request.user
            free.modify_date = timezone.now()  # 수정일시 저장
            free.save()
            return redirect('free:detail', free_id=free.id)
    else:
        form = FreeForm()
    context = {'form': form}
    return render(request, 'free/free_form.html', context)


# @login_required(login_url='common:login')
def free_delete(request, free_id):
    free = get_object_or_404(Free, pk=free_id)
    if request.user != free.writer:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('free/free:detail', free_id=free.id)
    free.delete()
    return redirect('free:index')

# 댓글등록
def comment_create_free(request, free_id):
    free = get_object_or_404(Free, pk=free_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.title = free
            comment.writer = request.user
            comment.create_date = timezone.now()
            # comment.free = free
            comment.save()
            return redirect('free:detail', free_id=free.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'free/comment_form.html', context)

#댓글 수정
def comment_modify_free(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.writer:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('free:detail', free_id=comment.title.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.writer = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('free:detail', free_id=comment.title.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'free/comment_form.html', context)

#댓글삭제
def comment_delete_free(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.writer:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('free:detail', free_id=comment.title.id)
    else:
        comment.delete()
    return redirect('free:detail', free_id=comment.title.id)

