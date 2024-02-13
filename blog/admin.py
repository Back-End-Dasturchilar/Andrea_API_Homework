from django.contrib import admin
from .models import (Category,
                     Post,
                     About,
                     Tag,
                     Travel)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created')
    list_display_links = ['id', 'title', 'created']



admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(About)
admin.site.register(Travel)

