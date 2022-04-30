from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.
class WIDoc(models.Model):
    class file_type_choice(models.IntegerChoices):
        RESUME = 1, 'Resume'
        COVERLETTER = 2, 'Cover Letter'
        INTRODUCTION = 3, 'Self Introduction'
        PORTFOLIO = 4, 'Portfolio'
        OTHER = 9, 'Other'
    doc_type = models.IntegerField(choices = file_type_choice.choices, default = file_type_choice.OTHER)
    doc_number = models.CharField(max_length = 30)
    doc_name = models.CharField(max_length = 255)
    doc_version = models.IntegerField()
    doc_date = models.DateField(auto_now=True)
    doc_attachment = models.FileField(upload_to='work_instruction/files/')

    def __str__(self):
        return self.doc_number

    # def get_absolute_url(self):
    #     return reverse("")

    class Meta:
        ordering = ["doc_type", "doc_number"]

class WIDoc_Revise(models.Model):
    doc_father = models.ForeignKey(WIDoc, related_name='doc_f', on_delete=models.CASCADE)
    doc_revision = models.IntegerField()
    doc_modify = models.TextField()
    doc_revisor = models.CharField(max_length = 100)
    doc_rev_date = models.DateField()

    # def __str__(self):
    #     return self.doc_revision
