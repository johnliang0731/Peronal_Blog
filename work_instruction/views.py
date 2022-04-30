from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.db.models import Q

from . import models
from .forms import WIDocForm, WIDocRevForm
# Create your views here.
class WIDocList(generic.ListView):
    model = models.WIDoc
    template_name = "work_instruction/index.html"

class WIDocDetail(generic.DetailView):
    model = models.WIDoc
    template_name = "work_instruction/widoc_detail.html"

def WIDocRevise(request, pk):
    post = get_object_or_404(models.WIDoc, pk=pk)
    if request.method == "POST":
        form = WIDocRevForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.doc_father = post
            comment.save()
            return redirect('work_instruction:detail', pk=pk)
    else:
        form = WIDocRevForm()
    return render(request, 'work_instruction/revise_form.html', {'form': form})

def WIDoc_upload(request):
    # post = get_object_or_404(models.WIDoc, pk=pk)
    if request.method == 'POST':
        form = WIDocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('work_instruction:index')
    else:
        form = WIDocForm()
    return render(request, 'work_instruction/widoc_form.html', {'form': form })

def WIDoc_update(request, pk):
    instance = get_object_or_404(models.WIDoc, pk=pk)
    form = WIDocForm(request.POST, request.FILES, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('work_instruction:index')
    return render(request, 'work_instruction/widoc_form.html', {'form': form })

def WISearch(request):
    q = request.GET.get("q")
    error_msg = ''
    if not q:
        error_msg = "Please input valid content"
        return render(request, "work_instruction/search_result.html",{'error_msg': error_msg})
    post_search = models.WIDoc.objects.filter(Q(doc_number__icontains=q) | Q(doc_name__icontains=q))
    return render(request, "work_instruction/search_result.html", {'error_msg': error_msg, 'post_search':post_search} )
