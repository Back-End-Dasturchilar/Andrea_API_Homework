from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(About)
admin.site.register(Archives)