from rest_framework import serializers
from .models import (Comment,
                     Category,
                     Author,
                     About,
                     Archives,
                     Tag,
                     Post)


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_field = ['created_at', 'update_at']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['created_at', 'update_at']


class AboutSeria(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        read_only_fields = ['created_at', 'update_at']


class ArchiveSer(serializers.ModelSerializer):
    class Meta:
        model = Archives
        fields = '__all__'


class TagSer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CommentSer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'post', 'name', 'email', 'website', 'message']


class PostSer(serializers.ModelSerializer):
    author = AuthorSerializer()
    tags = TagSer()
    comment = CommentSer

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'description', 'author', 'tags', 'comment']
        read_only_field = ['created_at', 'update_at']

