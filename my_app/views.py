from django.shortcuts import render
from rest_framework import generics
from .models import (Post,
                     Author,
                     About,
                     Tag,
                     Comment,
                     Category,
                     Archives,
                     )
from .serializers import (AuthorSerializer,
                          AboutSeria,
                          PostSer,
                          CommentSer,
                          CategorySerializers,
                          TagSer,
                          ArchiveSer,
                          )


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class TagView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSer


class ArchiveView(generics.ListAPIView):
    queryset = Archives.objects.all()
    serializer_class = ArchiveSer


class CommentView(generics.CreateAPIView):
    queryset = Comment
    serializer_class = CommentSer


class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSer


class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSeria


class AuthorView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

