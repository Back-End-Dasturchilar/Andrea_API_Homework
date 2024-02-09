from django.urls import path
from .views import ContactInfoView, CreateContact

urlpatterns = [
    path('', CreateContact.as_view()),
    path('info/', ContactInfoView.as_view())
]
