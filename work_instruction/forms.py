from django import forms
from . import models

class WIDocForm(forms.ModelForm):
    class Meta:
        fields = ("doc_type", "doc_number", "doc_name", "doc_version", "doc_attachment",)
        model = models.WIDoc

class DateInput(forms.DateInput):
    input_type = 'date'

class WIDocRevForm(forms.ModelForm):
    class Meta:
        model = models.WIDoc_Revise
        fields = ["doc_revision", "doc_modify", "doc_revisor", "doc_rev_date"]
        widgets = {
            "doc_rev_date": DateInput(),
        }
