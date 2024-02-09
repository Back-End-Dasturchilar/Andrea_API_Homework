from rest_framework import serializers
from .models import *


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'website', 'message']
        read_only = ['created_at']


class CantactInfoSer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['address', 'phone', 'website', 'message']
