from django import forms
from alog.models import Blogpost, Answer

class BlogpostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }