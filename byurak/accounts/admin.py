from django.contrib import admin
from accounts.models import User, Profile, UserFollow


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(UserFollow)