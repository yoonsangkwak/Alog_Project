from django import forms
from alog.models import Blogpost, Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }