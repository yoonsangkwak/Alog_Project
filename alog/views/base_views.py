from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from ..models import Blogpost
import logging

logger = logging.getLogger('alog')

# Create your views here.
def index(request):
    """
    메인 첫 페이지
    """
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    logger.info("INFO 레벨로 출력")
    # 조회
    post_list = Blogpost.objects.order_by('-create_date')
    if kw:
        post_list = post_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw)  # 내용검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(post_list, 10) # 10개씩
    page_obj = paginator.get_page(page)

    context = {'post_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'alog/post_list.html', context)


def detail(request, blogpost_id):
    """
    블로그 글 내용 출력
    """
    blogpost = get_object_or_404(Blogpost, pk=blogpost_id)
    context = {'blogpost': blogpost}
    return render(request, 'alog/post_detail.html', context)


def about(request):
    """
    About 페이지
    """
    context = {'about': about}
    return render(request, 'alog/about.html', context)


def contact(request):
    """
    Contact 페이지
    """
    context = {'contact': contact}
    return render(request, 'alog/contact.html', context)