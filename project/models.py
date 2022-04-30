from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Project(models.Model):

    class bus_type_choice(models.IntegerChoices):
        K7M = 1
        K8M = 2
        K9M = 3

    class module_type_choice(models.IntegerChoices):
        Traditional = 1
        LiquidCooling = 2
        Standardized = 3

    class project_status_choice(models.IntegerChoices):
        PO_PROCESSING = 1
        MATERIAL_DELIVERING = 2
        IN_STOCK = 3
        ON_PROCESS = 4
        FINISHED = 5
        PAUSED = 6
        CANCELLED = 7
        OTHER = 8

    bus_type = models.IntegerField(choices = bus_type_choice.choices)
    project_name = models.CharField(max_length = 255)
    module_type = models.IntegerField(choices = module_type_choice.choices)
    bus_number = models.IntegerField()
    reference_number = models.CharField(max_length = 20, blank = True)
    project_status = models.IntegerField(choices = project_status_choice.choices, null = True)

    class Meta:
        ordering = ["bus_type"]

    def get_absolute_url(self):
        return reverse("project:detail", kwargs={'pk':self.pk})

    def __str__(self):
        bustype = str(self.get_bus_type_display())
        return bustype + '-' + self.project_name

# class ProjectInfo(models.Model):
#     project_ref = models.IntegerField(null=True)
#     project_sap = models.CharField()


# upload
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='project/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    project_father = models.ForeignKey(Project, related_name="docu", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
