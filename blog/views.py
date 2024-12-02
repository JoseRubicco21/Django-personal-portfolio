from django.shortcuts import render, get_object_or_404
from .models import BlogPost


# Create your views here.
def blogs(request):
    blogposts = BlogPost.objects.order_by("-date")[:3]
    blog_count = BlogPost.objects.all().count()
    return render(request, "blog/home.html", {"blogs": blogposts, "number": blog_count})


def post(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, "blog/post.html", {"blog": blog})
