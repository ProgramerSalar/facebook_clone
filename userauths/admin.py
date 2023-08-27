from django.contrib import admin
from .models import User, Profile
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'email', 'gender']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'user', 'verified']
    list_editable = ['verified']

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)