from django.contrib import admin

from users.models import Profile, User

# Register your models here.

admin.site.register(User)
admin.site.register(Profile)