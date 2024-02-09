from django.contrib import admin
from app.models import *

# Register your models here.
class Mini(admin.TabularInline):
    model = MiniPost
    extra = 1


class Com(admin.TabularInline):
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    list_display_links = ['id','title']
    filter_horizontal = ['tag']
    inlines = [Mini, Com]

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(MiniPost)
admin.site.register(Comment)