from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import CreatePostForm, UpdatePostForm
from blog.models import Category, Post, UserProfile
from blog.utils import create_user
import pandas as pd

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
#
# def create_post(request):
#     if request.method == 'POST':
#         title = request.POST['post_title']
#         body = request.POST['post_content']
#         category_id = request.POST['category_id']
#         author_id = request.POST['author_id']
#         author = User.objects.get(id=author_id)
#
#         category = Category.objects.get(id=category_id)
#         post = Post.objects.create(title=title, category=category, body=body, author=author)
#         return redirect('post_detail', post_id=post.id)
#     return render(request, 'blog/create_post.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = UpdatePostForm
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        github_url = request.POST['github_url']
        linkedin_url = request.POST['linkedin_url']
        create_user(username, password, first_name, last_name, email, github_url, linkedin_url)
        return redirect('login')
    return render(request, 'registration/register.html')

def create_users(request):
    if request.method == 'POST' and request.FILES['names_files']:
        names_file = request.FILES['names_files']
        fs = FileSystemStorage()
        filename = fs.save(names_file.name, names_file)
        uploaded_file_url = fs.url(filename)
        uploaded_file_path = fs.path(filename)
        print(uploaded_file_path)
        excel_read = pd.read_excel(uploaded_file_path)
        data = pd.DataFrame(excel_read, columns=['username', 'password', 'first_name', 'last_name', 'email', 'github_url', 'linkedin_url'])
        print(data)
        for index, row in data.iterrows():
            if User.objects.filter(username=row['username']).exists():
                user = User.objects.get(username=row['username'])
                user.delete()
            create_user(row['username'], row['password'], row['first_name'], row['last_name'], row['email'], row['github_url'], row['linkedin_url'])
        return render(request, 'blog/create_user.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'blog/create_user.html')

def login(request):
    return render(request, 'registration/login.html')

def logout(request):
    return render(request, 'registration/logout.html')
