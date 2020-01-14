from django.views import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from blog.models import Post,Comment
from blog.forms import PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/' #login page
    redirect_field_name = 'blog/post_detail.html' #defined in mixin
    form_class = PostForm #form to be shown for login
    model = Post 

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/' #login page
    redirect_field_name = 'blog/post_detail.html' #defined in mixin
    form_class = PostForm #form to be shown for login
    model = Post 

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/' #login page
    redirect_field_name = 'blog/post_detail.html' #defined in mixin
    model = Post 

    def get_queryset(self):
        return Post.objects.filter(published_date_isnull=True).order_by('created_date')
