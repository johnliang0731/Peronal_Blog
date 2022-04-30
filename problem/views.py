from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from . import models
from .forms import PostAttachForm, ReplyAttachForm, ReplyForm

from django.contrib.auth import get_user_model
User = get_user_model

from django.db.models import Q

# Create your views here.

class PostList(generic.ListView):
    model = models.Post

class PostDetail(generic.DetailView):
    model = models.Post
    # context_object_name = 'problem_detail'

class CreatePost(LoginRequiredMixin, generic.CreateView):
    fields = ('title', 'status', 'description',)
    model = models.Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

def postform_upload(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    if request.method == 'POST':
        form = PostAttachForm(request.POST, request.FILES)
        if form.is_valid():
            docum = form.save(commit=False)
            docum.post_father = post
            docum.save()
            return redirect('problem:postdetail', pk=pk)
    else:
        form = PostAttachForm()
    return render(request, 'problem/postform_upload.html', {'form': form })

# class UpdatePost(LoginRequiredMixin, generic.UpdateView):
#     fields = ("status",)
#     model = models.Post

def post_status_change(request, pk):
    post_content = get_object_or_404(models.Post, pk=pk)
    if post_content.status == 2 or post_content.status == 3:
        post_content.status = 1
    else:
        post_content.status = 2
    post_content.save()
    return redirect("problem:postdetail", pk=post_content.pk)

def post_status_highlight(request, pk):
    post_content = get_object_or_404(models.Post, pk=pk)
    post_content.status = 3
    post_content.save()
    return redirect("problem:postdetail", pk=post_content.pk)

class DeletePost(LoginRequiredMixin, generic.DeleteView):
    model = models.Post
    success_url = reverse_lazy("problem:all")

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted!")
        return super().delete(*args, **kwargs)

def create_reply_to_post(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('problem:postdetail', pk=post.pk)
    else:
        form = ReplyForm()
    return render(request, 'problem/reply_form.html', {'form': form})

def replyform_upload(request, pk):
    reply = get_object_or_404(models.Reply, pk=pk)
    if request.method == 'POST':
        form = ReplyAttachForm(request.POST, request.FILES)
        if form.is_valid():
            docum = form.save(commit=False)
            docum.reply_father = reply
            docum.save()
            return redirect('problem:all')
    else:
        form = ReplyAttachForm()
    return render(request, 'problem/replyform_upload.html', {'form': form })

class DeleteReply(LoginRequiredMixin, generic.DeleteView):
    model = models.Reply
    success_url = reverse_lazy("problem:all")

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Reply Deleted!")
        return super().delete(*args, **kwargs)

def PostSearch(request):
    q = request.GET.get("q")
    error_msg = ''
    if not q:
        error_msg = "Please input valid content"
        return render(request, "problem/search_result.html",{'error_msg': error_msg})
    post_search = models.Post.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
    return render(request, "problem/search_result.html", {'error_msg': error_msg, 'post_search':post_search} )
