from django.contrib import admin
from django.contrib.auth.models import Group

from accounts.models import User, Interest

# admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Interest)

