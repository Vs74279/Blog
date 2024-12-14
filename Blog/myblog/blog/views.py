from django.shortcuts import render, redirect
from .models import Category, Post
from .forms import CategoryForm, PostForm

# Create Category View
from django.shortcuts import render, redirect
from .forms import CategoryForm

def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category_list')  # Redirect to the category list after saving
    else:
        form = CategoryForm()
    
    return render(request, 'blog/create_category.html', {'form': form})


# Create Post View
def create_post(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form, 'categories': categories})

# List Posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

# Post Detail View
def post_detail(request, post_id):
    post = Post.objects.get(post_id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

# List Categories
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})
