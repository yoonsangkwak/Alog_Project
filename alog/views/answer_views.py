from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..models import Blogpost, Answer

def answer_create(request, blogpost_id):
    """
    댓글등록
    """
    blogpost = get_object_or_404(Blogpost, pk=blogpost_id)
    blogpost.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('alog:detail', blogpost_id=blogpost.id)