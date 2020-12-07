from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..models import Blogpost, Answer
from ..forms import AnswerForm

def answer_create(request, blogpost_id):
    """
    댓글등록
    """
    blogpost = get_object_or_404(Blogpost, pk=blogpost_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.blogpost = blogpost
            answer.save()
            return redirect('alog:detail', blogpost_id=blogpost.id)
    else:
        form = AnswerForm()
    context = {'blogpost': blogpost, 'form': form}
    return render(request, 'alog/post_detail.html', context)