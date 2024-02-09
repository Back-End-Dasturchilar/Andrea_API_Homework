from rest_framework.serializers import ModelSerializer
from app.models import *



class TagApi(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class CatApi(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']



class AthorApi(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class PostApi(ModelSerializer):
    tag = TagApi
    category = CatApi
    author = AthorApi
    class Meta:
        model = Post
        fields = ['title','img','category','tag','created_at','author']


class MiniApi(ModelSerializer):
    mini = PostApi
    class Meta:
        model = MiniPost
        fields = ['title','img','desc_up','desc_bottom','mini']


class ComApi(ModelSerializer):
    writer = AthorApi
    post = PostApi
    class Meta:
        model = Comment
        fields = ['writer','post','msg','created_at']




