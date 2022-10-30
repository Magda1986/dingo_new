from django.shortcuts import render
from .models import Post, Author
from .forms import PostForm, AuthorForm
from django.http import HttpResponse
from django.template import loader



def new_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save(commit = True)
        form = PostForm
    context = {
        "form": form
    }
    return render(request, "posts/new_post.html", context)

def new_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        form = AuthorForm
    context = {
        "form": form
    }
    return render(request, "posts/new_author.html", context)

def post(request):
    t = loader.get_template("posts/main.html")
    return HttpResponse(t.render())


def posts_list(request):
    posts = Post.objects.all()
    form = PostForm()
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()      # tutaj wprowadzamy zmianę
            messages.add_message(
                request,
                messages.SUCCESS,
                "Dodano nowy Post!!"
            )

#def posts_list(request):
    #t = loader.get_template("posts/posts_list.html")
    #return HttpResponse(t.render())

def post_details(request):
    t = loader.get_template("posts/post_details.html")
    return HttpResponse(t.render())

def authors_list(request):
    t = loader.get_template("posts/authors_list.html")
    return HttpResponse(t.render())

def author_details(request):
    t = loader.get_template("posts/author_details.html")
    return HttpResponse(t.render())



#posts_list, post_details, authors_list, author_details
