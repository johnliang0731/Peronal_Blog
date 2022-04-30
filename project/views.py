from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from project import models
from .forms import DocumentForm

from django.utils.http import urlquote
from django.http import FileResponse
# Create your views here.
class Project_List(generic.ListView):
    model = models.Project
    template_name = "project/project_index.html"

class Create_Project(generic.CreateView):
    model = models.Project
    fields = ("bus_type", "project_name", "module_type", "bus_number",
    "reference_number", "project_status",)

class Project_DetailView(generic.DetailView):
    context_object_name = 'project_detail'
    model = models.Project
    template_name = 'project/project_detail.html'

class Project_UpdateView(generic.UpdateView):
    fields = ("bus_type", "project_name", "module_type", "bus_number",
    "reference_number", "project_status",)
    model = models.Project

class Project_DeleteView(generic.DeleteView):
    model = models.Project
    success_url = reverse_lazy("project:index")



# upload, 通过get_object来取得project的foreignkey，然后传给form
def model_form_upload(request, pk):
    post = get_object_or_404(models.Project, pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            docum = form.save(commit=False)
            docum.project_father = post
            docum.save()
            return redirect('project:detail', pk=pk)
    else:
        form = DocumentForm()
    return render(request, 'project/model_form_upload.html', {'form': form })

# 直接删除，没有确认
def document_delete(request, pk):
    attachment = get_object_or_404(models.Document, pk=pk)
    attach_pk = attachment.project_father.pk
    attachment.delete()
    return redirect('project:detail', pk=attach_pk)

# 尝试新的upload写法
# def model_form_upload(request, pk):
#     post = get_object_or_404(models.Project, pk=pk)
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             docum = form.save(commit=False)
#             docum.project_father = post
#             docum.save()
#             destination = open(os.path.join("project/", docum.name), 'wb+')
#             for chunk in docum.chunks():
#                 destination.write(chunk)
#             destination.close()
#             return redirect('project:detail', pk=pk)
#     else:
#         form = DocumentForm()
#     return render(request, 'project/model_form_upload.html', {'form': form })
#
# def download(request, id):
#     doc_info = models.Document.objects.get(id=id)
#     file = open(doc_info.file_path, 'rb')
#     response = FileResponse(file)
#     response['Content-Disposition'] = 'attachment; filename="%s"' % urlquote(doc_info.file_name)
