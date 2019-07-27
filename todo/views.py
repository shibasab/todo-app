from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

def home(request):
    return render(request, 'home.html')

def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now(), user=request.user).order_by('created_date')
    return render(request, 'todo/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user == request.user:
        return render(request, 'todo/post_detail.html', {'post': post})
    else:
        # ここにエラーメッセージを出したい
        return redirect('post_list')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.user = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'todo/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user == request.user:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.created_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'todo/post_edit.html', {'form': form})
    else:
        # ここにエラーメッセージを出したい
        return redirect('post_list')