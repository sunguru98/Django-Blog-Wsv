from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import BlogPost
# Create your views here.


class IndexPageTemplateView(ListView):
    model = BlogPost
    template_name = 'home.html'
    context_object_name = "posts"

class BlogPostListView(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = "blog_post_list.html"
    context_object_name = "posts"


class BlogPostDetailView(LoginRequiredMixin, DetailView):
    model = BlogPost
    template_name = "blog_post_detail.html"
    context_object_name = "post"


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = "blog_post_create.html"
    fields = "__all__"


class BlogPostEditView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    template_name = "blog_post_update.html"
    fields = ("title", "body")


class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = "blog_post_delete.html"
    success_url = reverse_lazy("blog_list")