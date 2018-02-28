from django.db import models

# Create your models here.

class Post(models.Model):
    """A model class for post"""

    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(max_length=50)
    #image = models.ImageField(upload_to='uploads/')
    author = models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE
    )

    created_at =  models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

