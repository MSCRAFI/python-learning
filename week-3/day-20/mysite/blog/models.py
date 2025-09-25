from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200) # Title of the blog post
    content = models.TextField() # Content of the blog post
    created_at = models.DateTimeField(auto_now_add=True) # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True) # Date and time of last update

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title