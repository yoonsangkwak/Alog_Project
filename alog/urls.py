from django.urls import path

from .views import base_views, answer_views

app_name = 'alog'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:blogpost_id>/', base_views.detail, name='detail'),

    # answer_views.py
    path('answer/create/<int:blogpost_id>/', answer_views.answer_create, name='answer_create'),
]