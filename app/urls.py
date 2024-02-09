from django.urls import path,include
from app.views import PostList,ComList,TagList,CatList,MiniPostList

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('com/', ComList.as_view(), name='com'),
    path('tag/', TagList.as_view(), name='tag'),
    path('cat/', CatList.as_view(), name='cat'),
    path('mini/', MiniPostList.as_view(), name='mini'),
    path('detail/<int:pk>/', PostList.as_view(), name='detail'),
]