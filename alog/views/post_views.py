from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..models import Blogpost
from ..forms import BlogpostForm

@login_required(login_url='common:login')
def post_create(request):
    """
    블로그 글 쓰기
    """
    if request.method == 'POST':
        form = BlogpostForm(request.POST)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.create_date = timezone.now()
            blogpost.save()
            return redirect('alog:index')
    else:
        form = BlogpostForm()
    context = {'form': form}
    return render(request, 'alog/post_form.html', context)


@login_required(login_url='common:login')
def post_modify(request, blogpost_id):
    """
    블로그 글 수정
    """
    blogpost = get_object_or_404(Blogpost, pk=blogpost_id)
    if request.user != blogpost.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('alog:detail', blogpost_id=blogpost.id)

    if request.method == "POST":
        form = BlogpostForm(request.POST, instance=blogpost)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.modify_date = timezone.now()
            blogpost.save()
            return redirect('alog:detail', blogpost_id=blogpost.id)
    else:
        form = BlogpostForm(instance=blogpost)
    context = {'form': form}
    return render(request, 'alog/post_form.html', context)


@login_required(login_url='common:login')
def post_delete(request, blogpost_id):
    """
    블로그 글 삭제
    """
    blogpost = get_object_or_404(Blogpost, pk=blogpost_id)
    if request.user != blogpost.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('alog:detail', blogpost_id=blogpost.id)
    blogpost.delete()
    return redirect('alog:index')