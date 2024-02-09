from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from app.serialaziers import *
from app.models import *

# Create your views here.
class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostApi

class MiniPostList(ListAPIView):
    queryset = MiniPost.objects.all()
    serializer_class = MiniApi

class TagList(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagApi


class CatList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CatApi


class ComList(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = ComApi


class ComList(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostApi
