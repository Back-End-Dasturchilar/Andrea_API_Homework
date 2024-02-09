from django.urls import path
from .views import (CategoryView,
                    TagView,
                    AboutView,
                    ArchiveView,
                    AuthorView,
                    CommentView,
                    PostView,
                    )

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('tags/', TagView.as_view()),
    path('about/', AboutView.as_view()),
    path('author/', AuthorView.as_view()),
    path('archive/', ArchiveView.as_view()),
    path('commit/', CommentView.as_view()),
    path('post/', PostView.as_view())
]