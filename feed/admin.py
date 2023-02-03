from django.contrib import admin
from .models import Post

class Postadmin(admin.ModelAdmin):
    pass

admin.site.register(Post, Postadmin)
