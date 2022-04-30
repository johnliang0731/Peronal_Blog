from django.db import models
from django.conf import settings
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Post(models.Model):
    class status_choice(models.IntegerChoices):
        WORK = 1, 'Work'
        STUDY = 2, 'Study'
        LIFE = 3, 'Life'
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.IntegerField(choices = status_choice.choices, default=status_choice.LIFE)
    title = models.CharField(max_length = 255)
    create_date = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("problem:postdetail", kwargs={'pk':self.pk})

    class Meta:
        ordering = ["-status", "-create_date"]

class Post_Attachment(models.Model):
    description = models.CharField(max_length=255, blank=True)
    postattach = models.ImageField(upload_to='problem/post/')
    uploaded_at = models.DateTimeField(auto_now=True)
    post_father = models.ForeignKey(Post, related_name="post_f", on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class Reply(models.Model):
    post = models.ForeignKey(Post, related_name='replys', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reply_date = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("problem:all")


class Reply_Attachment(models.Model):
    description = models.CharField(max_length=255, blank=True)
    replyattach = models.FileField(upload_to='problem/reply')
    uploaded_at = models.DateTimeField(auto_now=True)
    reply_father = models.ForeignKey(Reply, related_name="reply_f", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
