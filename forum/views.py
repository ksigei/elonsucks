from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ForumPost, ForumPicture
from .forms import ForumPostForm, ForumPictureForm

def forum_post_list(request):
    posts = ForumPost.objects.all()
    return render(request, 'forum/forum_post_list.html', {'posts': posts})

@login_required
def create_forum_post(request):
    if request.method == 'POST':
        post_form = ForumPostForm(request.POST)
        picture_form = ForumPictureForm(request.POST, request.FILES)
        if post_form.is_valid() and picture_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            for picture in request.FILES.getlist('pictures'):
                ForumPicture.objects.create(forum_post=post, picture=picture)
            return redirect('forum_home')  # Redirect to the forum homepage
    else:
        post_form = ForumPostForm()
        picture_form = ForumPictureForm()
    return render(request, 'forum/create_forum_post.html', {'post_form': post_form, 'picture_form': picture_form})

@login_required
def forum_post_detail(request, pk):
    post = get_object_or_404(ForumPost, pk=pk)
    return render(request, 'forum/forum_post_detail.html', {'post': post})

@login_required
def update_forum_post(request, pk):
    post = get_object_or_404(ForumPost, pk=pk)
    if request.method == 'POST':
        post_form = ForumPostForm(request.POST, instance=post)
        picture_form = ForumPictureForm(request.POST, request.FILES)
        if post_form.is_valid() and picture_form.is_valid():
            post = post_form.save(commit=False)
            post.save()
            for picture in request.FILES.getlist('pictures'):
                ForumPicture.objects.create(forum_post=post, picture=picture)
            return redirect('forum_post_detail', pk=pk)  # Redirect to the post detail page
    else:
        post_form = ForumPostForm(instance=post)
        picture_form = ForumPictureForm()
    return render(request, 'forum/update_forum_post.html', {'post_form': post_form, 'picture_form': picture_form})

@login_required
def delete_forum_post(request, pk):
    post = get_object_or_404(ForumPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('forum_home')  # Redirect to the forum homepage
    return render(request, 'forum/delete_forum_post.html', {'post': post})

