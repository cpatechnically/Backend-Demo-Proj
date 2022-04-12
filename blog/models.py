from django.db import models
from django.utils import timezone
#author = the user that created the post
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #first time posted/created date time
    date_posted = models.DateTimeField(default=timezone.now)
    #forign key because the author is a FK of the User model. 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #last modified
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    #
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})