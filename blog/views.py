
from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from . import email_DJG as email


def post_list(request):
    posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    paginator = Paginator(posts_list, 10)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'posts': posts})


# *****************************************************************************
# def listing(request):
#     contact_list = Contacts.objects.all()
#     paginator = Paginator(contact_list, 25) # Show 25 contacts per page
#
#     page = request.GET.get('page')
#     try:
#         contacts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         contacts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         contacts = paginator.page(paginator.num_pages)
#
#     return render(request, 'list.html', {'contacts': contacts})
# *****************************************************************************


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments_list = post.comments.all()

    paginator = Paginator(comments_list, 4)

    page = request.GET.get('page')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comments = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comments = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog.views.post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            ip = request.META.get('REMOTE_ADDR')  # Get client IP
            remote_ip = ip
            # print "views remote_ip=", remote_ip

            # *****************************************************************
            email_subject = unicode("[" + remote_ip + "] " + comment.post.title)
            email_body = unicode(comment.author + "\n <b>says:</b> \n" + comment.text)
            email_body = email_body.encode('ascii', 'xmlcharrefreplace')
            # print "comment.post=", email_subject, email_body
            email.my_email(email_subject, email_body, ["20flint12@gmail.com"])
            # *****************************************************************

            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})














@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)


###############################################################################

def services(request):
    return render(request, 'templates/static_pages/services_page.html')


def contacts(request):
    # text = "<h2>email:</h2><h1>email: plechan121@gmail.com</h1>"
    # return HttpResponse(text)
    return render(request, 'templates/static_pages/contacts_page.html')


def plan(request):
    # text = "<h2>email:</h2><h1>email: plechan121@gmail.com</h1>"
    # return HttpResponse(text)

    flats = range(338, 0, -1)
    floors = 26

    return render(request, 'templates/static_pages/building_plan.html', {'flats': flats, 'floors': floors})


def adv(request):
    return render(request, 'templates/static_pages/building_adv.html')


def rates(request):
    return render(request, 'templates/static_pages/rates.html')


def deputy(request):
    return render(request, 'templates/static_pages/deputy.html')















