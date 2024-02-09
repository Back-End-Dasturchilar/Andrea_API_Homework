from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    website = models.CharField(max_length=212)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    address = models.CharField(max_length=212)
    phone = models.CharField(max_length=212)
    email = models.EmailField()
    website = models.CharField(max_length=212)

    def __str__(self):
        return self.address


