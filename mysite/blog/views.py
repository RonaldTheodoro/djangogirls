from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from mysite.blog.models import Post
from mysite.blog.forms import PostForm


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mysite.blog.views.post_detail', pk=post.pk)

    else:
        form = PostForm()

    return render(request, 'post_new.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mysite.blog.views.post_detail', pk=post.pk)

    else:
        form = PostForm()

    return render(request, 'post_new.html', {'form': form})