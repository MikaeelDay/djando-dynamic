from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm

def home(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'home.html', {'posts': posts})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter(active=True).order_by('-created_on')
    count_comments = comments.count()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.post = post
            comment.name = form.cleaned_data['username']
            comment.body = form.cleaned_data['comment']
            comment.save()
            return redirect('detail', id=post.id)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': form,
        'count_comments': count_comments
    }

    return render(request, 'detail.html', context)
