from django.shortcuts import render, redirect, reverse
from .models import BlogPost, Comment, Contact
from .forms import CommentForm, CreatePostForm, ContactForm
from django.http import HttpResponseForbidden
import math
import os


def superuser_only(f):
    def wrapped_function(request, *args, **kwargs):
        if request.user.is_superuser:
            return f(request, *args, **kwargs)
        return HttpResponseForbidden()
    return wrapped_function


# Create your views here.
def get_all_posts(request):
    context = {'img_url': os.environ.get("HOME_IMG_URL"), 'heading': os.environ.get("HOME_HEADING"),
               'subheading': os.environ.get("HOME_SUBHEADING", "A collection of basically nothing.")}
    page_number = int(request.GET.get('page_number', 1))
    context['page_number'] = page_number
    posts = BlogPost.objects.all().order_by("id")
    posts.reverse()
    if len(posts) - 5*(page_number-1) > 5:
        posts = posts[(page_number-1)*5:(page_number-1)*5 + 5]
    else:
        posts = posts[(page_number-1)*5:]
    context['all_posts'] = posts
    context['max_page'] = math.ceil(len(posts)/5)
    context['next_page'] = context['max_page'] > page_number
    context['prev_page'] = page_number > 1
    return render(request, "main/index.html", context)


def show_post(request, post_id):
    requested_post = BlogPost.objects.get(id=post_id)
    requested_post.views += 1
    requested_post.save()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                comment = Comment(
                    comment_author=request.user,
                    parent_post=requested_post,
                    text=form.cleaned_data.get('comment_text')
                )
                comment.save()
                return redirect(reverse("show_post", kwargs={"post_id": post_id}))
    form = CommentForm()
    return render(request, "main/post.html", {"post": requested_post, "form": form})


@superuser_only
def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            new_post = BlogPost(
                title=form.cleaned_data.get('title'),
                subtitle=form.cleaned_data.get('subtitle'),
                body=form.cleaned_data.get('body'),
                img_url=form.cleaned_data.get('img_url'),
                author=request.user,
                views=0,
            )
            new_post.save()
            return redirect(reverse("home"))
    form = CreatePostForm()
    return render(request, "main/make-post.html", {"form": form})


@superuser_only
def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data.get('title')
            post.subtitle = form.cleaned_data.get('subtitle')
            post.img_url = form.cleaned_data.get('img_url')
            post.body = form.cleaned_data.get('body')
            post.save()
            if post.id == 1:
                return redirect(reverse('about'))
            return redirect(reverse('show_post', kwargs={'post_id': post_id}))
    else:
        initial_dict = {
            "title": post.title,
            "subtitle": post.subtitle,
            "img_url": post.img_url,
            "body": post.body,
        }
        form = CreatePostForm(initial=initial_dict)
    return render(request, "main/make-post.html", {'form': form})


def about(request):
    return render(request, "main/about.html", {'post': BlogPost.objects.get(id=1)})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = Contact(
                email=form.cleaned_data.get('email'),
                name=form.cleaned_data.get('username'),
                phone_number=form.cleaned_data.get('phone_number'),
                message=form.cleaned_data.get('message'),
            )
            new_contact.save()
            form = ContactForm()
    else:
        initial_dict = None
        if request.user.is_authenticated:
            initial_dict = {
                "username": request.user.get_full_name(),
                "email": request.user.email
            }
            print(initial_dict)
        form = ContactForm(initial=initial_dict)
    return render(request, "main/contact.html", {"form": form})

