from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notice', views.notice_detail, name='notice_detail'),
    path('noticelist', views.notice_list, name='notice_list'),
    path('notice/search', views.notice_search, name='notice_search'),
]