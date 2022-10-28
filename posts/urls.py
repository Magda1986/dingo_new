from django.urls import path
from .views import post, posts_list, post_details, authors_list, author_details, new_post

app_name="posts"

urlpatterns = [
   path('', post),
   path('1', posts_list),
   path('2', post_details),
   path('3', authors_list),
   path('4', author_details),
   path('5', new_post),
   #path('posts', posts_list, name="post_list"))
]