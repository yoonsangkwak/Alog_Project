from django.urls import path

from .views import base_views, post_views, answer_views, comment_views

app_name = 'alog'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:blogpost_id>/', base_views.detail, name='detail'),
    path('about/', base_views.about, name='about'),
    path('contact/', base_views.contact, name='contact'),

    # post_views.py
    path('post/create/', post_views.post_create, name='post_create'),
    path('post/modify/<int:blogpost_id>/', post_views.post_modify, name='post_modify'),
    path('post/delete/<int:blogpost_id>/', post_views.post_delete, name='post_delete'),

    # answer_views.py
    path('answer/create/<int:blogpost_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

    # comment_views.py
    path('comment/create/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),
]