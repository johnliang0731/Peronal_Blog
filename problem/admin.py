from django.contrib import admin
from .models import Post, Reply, Post_Attachment, Reply_Attachment
# Register your models here.
admin.site.register(Post)
admin.site.register(Post_Attachment)
admin.site.register(Reply)
admin.site.register(Reply_Attachment)
