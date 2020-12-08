from django.urls import path

from .views import base_views, answer_views

app_name = 'alog'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:blogpost_id>/', base_views.detail, name='detail'),

    # answer_views.py
    path('answer/create/<int:blogpost_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
]