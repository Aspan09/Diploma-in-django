from django.contrib import admin
from .models import Post, Comment, UserNet, Message

admin.site.register(UserNet)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Message)
