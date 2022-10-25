from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



def post(request):
    t = loader.get_template("posts/main.html")
    return HttpResponse(t.render())

def posts_list(request):
    t = loader.get_template("posts/posts_list.html")
    return HttpResponse(t.render())

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
