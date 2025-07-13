from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Notice

def home(request):
    notices = Notice.objects.order_by('-created_at')[:5]
    return render(request, 'main/index.html', {'notices': notices})

def notice_detail(request):
    notice_id = request.GET.get('id')
    notice = get_object_or_404(Notice, id=notice_id)
    return render(request, 'main/notice_detail.html', {'notice': notice})

def notice_list(request):
    notices = Notice.objects.order_by('-created_at')
    return render(request, 'main/notice_list.html', {'notices': notices})

def notice_search(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = Notice.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)     #제목 내용 검색 기능 추가
        )

    return render(request, 'main/notice_search.html', {
        'query': query,
        'results': results,
    })