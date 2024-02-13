from django.shortcuts import render
from rest_framework import generics
from .models import (Post,
                     Category,
                     Tag,
                     Travel,
                     About)
from .serializer import (CategorySerializer,
                         TagSerializer,
                         PostSerializer,
                         TravelSerializer,
                         AboutSerializer)



class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TravelAPIView(generics.ListAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

class AboutAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class HomeAPIView(generics.ListAPIView):
    queryset = Post.objects.all()[:9]
    serializer_class = PostSerializer


class DetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer









