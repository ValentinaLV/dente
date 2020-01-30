from django.urls import path

from .views import NewsDetail
from .views import news_list, like_news, unlike_news, leave_comment


urlpatterns = [
    path('', news_list, name='news-details'),
    path('post/<str:slug>/', NewsDetail.as_view(), name='news-details'),
    path('post/<str:slug>/like/', like_news, name="like-news"),
    path('post/<str:slug>/unlike/', unlike_news, name="unlike-news"),
    path('post/<str:slug>/comment/', leave_comment, name="leave-comment-news"),
]

