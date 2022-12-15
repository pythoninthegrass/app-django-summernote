from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Post, PostAdmin)
