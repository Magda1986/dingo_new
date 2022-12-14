
#from django.db.models import Model
from django.db import models
class Post(models.Model):
    #id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        "posts.Author",
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    #def __str__(self):
        #return f"id:{self.id}, title:{self.title}, author:{self.author}"

class Author(models.Model):
    nick = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    #def __str__(self):
        #return f"nick:{self.nick}, email:{self.email}"
