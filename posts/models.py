from django.db import models
#from django.db.models import Model
#(znalezione w internecie przy przykladzie stosowania EmailFiled()

class Post(models.Model):
    #id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created = models.DateTimeFiled(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.EmailField(max_length=50)

class Author(models.Model):
    nick = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)

# Create your models here.
