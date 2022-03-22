from contextlib import nullcontext
from distutils.command.upload import upload
from venv import create
from django.db import models
from django.forms import SlugField
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    img = models.ImageField(upload_to='posts',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)

    

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"slug": self.slug})   


class Imagens(models.Model):
    banner = models.ImageField(upload_to='banner', null=True, blank=True)         
    logo = models.ImageField(upload_to='logo', null=True,blank=True)  