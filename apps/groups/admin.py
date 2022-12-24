from django.contrib import admin
from .models import Group, UserSendMessageInGroup


admin.site.register(UserSendMessageInGroup)
admin.site.register(Group)
