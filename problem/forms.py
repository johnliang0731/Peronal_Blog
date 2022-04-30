from django import forms
from . import models

class PostAttachForm(forms.ModelForm):
    class Meta:
        fields = ("description", "postattach",)
        model = models.Post_Attachment

class ReplyAttachForm(forms.ModelForm):
    class Meta:
        fields = ("description", "replyattach",)
        model = models.Reply_Attachment

class ReplyForm(forms.ModelForm):
    class Meta:
        model = models.Reply
        fields = ('description',)
