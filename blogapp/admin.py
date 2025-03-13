from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Blog

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "bio", "profile_picture",
                    "youtube", "facebook", "instagram", "twitter")
admin.site.register(CustomUser, CustomUserAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_draft", "created_date")
admin.site.register(Blog, BlogAdmin)