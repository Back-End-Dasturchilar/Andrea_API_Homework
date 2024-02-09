from django.shortcuts import render
from rest_framework import generics
from .serializers import ContactSerializers, CantactInfoSer
from .models import Contact, ContactInfo


class CreateContact(generics.CreateAPIView):
    queryset = Contact
    serializer_class = ContactSerializers


class ContactInfoView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = CantactInfoSer
