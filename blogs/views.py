
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, Category, Comment
from django.db.models import Q


def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='Published', category=category_id)

    # Use get_object_or_404 when you want to show 404 error page if the category does not exist
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)


def blogs(request, slug):
    # Fetch the specific blog post by slug
    blog_post = get_object_or_404(Blog, slug=slug, status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.blog = blog_post
        comment.user = request.user
        comment.comment = request.POST['comment']
        comment.save()
        return redirect('blogs', slug=slug)

    #comments
    comments = Comment.objects.filter(blog=blog_post)
    comment_count = comments.count()

    context = {
        'blog_post': blog_post,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'blogs.html', context)
def search(request):
    keyword = (request.GET.get('keyword') or '').strip()
    blogs = Blog.objects.none()
    if keyword:
        blogs = Blog.objects.filter(
            (Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword))
            & Q(status='Published')
        )

    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)