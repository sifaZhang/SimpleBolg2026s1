from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from blog.models import Category, Post


# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, 'blog/index.html', {'categories': categories})

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request, 'blog/category.html', {'category': category})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post.html', {'post': post})

def create_category(request):
    if request.method == 'POST':
        name = request.POST['category_name']
        category = Category.objects.create(name=name)
        return redirect('category_detail', category_id=category.id)
    return render(request, 'blog/create_category.html')

def create_post(request):
    if request.method == 'POST':
        title = request.POST['post_title']
        body = request.POST['post_content']
        category_id = request.POST['category_id']
        author_id = request.POST['author_id']
        author = User.objects.get(id=author_id)

        category = Category.objects.get(id=category_id)
        post = Post.objects.create(title=title, category=category, body=body, Auther=author)
        return redirect('post_detail', post_id=post.id)
    return render(request, 'blog/create_post.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'



