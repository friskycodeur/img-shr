from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User

class PostListView(ListView):
    model = Post
    template_name='home.html'
    context_object_name = 'posts'
    ordering=['-date_posted']
    paginate_by= 4

class PostDetailView(DetailView):
    model=Post
    template_name='post/post_detail.html'


class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['caption','image',]
    template_name='post/post_form.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    fields=['caption','image',]
    template_name='post/post_form.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template_name='post/post_confirm_delete.html'
    success_url='/'

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False