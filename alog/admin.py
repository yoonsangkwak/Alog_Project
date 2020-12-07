from django.contrib import admin
from .models import Blogpost
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Blogpost, PostAdmin)