from django.shortcuts import render, redirect, get_object_or_404
from tips.models import Tip
from django.core.paginator import Paginator

def index(request):
    tips_list = Tip.objects.all().order_by('-created_date')
    page = request.GET.get('page', '1')
    paginator = Paginator(tips_list, 5)
    page_obj = paginator.get_page(page)

    context = {'tips_list' : page_obj}
    return render(request, 'tips/tips_list.html', context)

def detail(request, tips_id):
    tips = get_object_or_404(Tip, pk=tips_id)
    context = {'tips' : tips}
    return render(request, 'tips/tips_detail.html', context)

