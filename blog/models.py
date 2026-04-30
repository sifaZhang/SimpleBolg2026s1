from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models. ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    post_date = models.DateField(auto_now_add=True)
    snippet = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return self.category.name + ' - ' + self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='images/')
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_body = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
