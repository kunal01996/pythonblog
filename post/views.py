from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'


class NewPostView(CreateView):
    model = Post
    template_name = 'create.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(NewPostView, self).get_context_data(**kwargs)
        context['users'] = get_user_model().objects.all()
        return context


def create(request):
    title = request.POST['title']
    body = request.POST['body']
    author = request.POST['author']
    status = request.POST['status']

    if status == 'on':
        status = True
    else:
        status = False

    Post.objects.create(
        title=title,
        body=body,
        author=get_user_model().objects.get(id=author),
        status=status
    )

    return HttpResponseRedirect(reverse('posts_list'))
