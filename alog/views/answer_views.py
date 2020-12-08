from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from ..models import Blogpost, Answer
from ..forms import AnswerForm

@login_required(login_url='common:login')
def answer_create(request, blogpost_id):
    """
    댓글등록
    """
    blogpost = get_object_or_404(Blogpost, pk=blogpost_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.blogpost = blogpost
            answer.save()
            return redirect('{}#answer_{}'.format(resolve_url('alog:detail', blogpost_id=blogpost.id), answer.id))
    else:
        form = AnswerForm()
    context = {'blogpost': blogpost, 'form': form}
    return render(request, 'alog/post_detail.html', context)


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
    댓글수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('alog:detail', blogpost_id=answer.blogpost.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(resolve_url('alog:detail', blogpost_id=answer.blogpost.id), answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'alog/answer_form.html', context)


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """
    댓글삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('alog:detail', blogpost_id=answer.blogpost.id)