from django.contrib import admin
from .models import Post
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from insta import models

# Register your models here.

admin.site.register(Post)

class UserAdmin(DjangoUserAdmin):

    date_hierachy = 'date_joined'
    ordering = ['-date_joined']
    list_display = list(DjangoUserAdmin.list_display) + ['date_joined']

admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    date_hierachy = 'created_at'
    ordering = ['-created_at']
    list_display = ['caption', 'user', 'created_at']
    search_fields = ['caption', 'user__username']
