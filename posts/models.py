from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    image_filter_choices = [
    ('movie', 'Movie'), ('series', 'Series'),
    ('comedy', 'Comedy'), ('drama', 'Drama'),
    ('animation', 'Animation'), ('horror', 'Horror'),
    ('action', 'Action'), ('science fiction', 'Science Fiction'),
    ('thriller', 'Thriller'), ('western', 'Western'),
    ('documentary', 'Documentary'), ('musical', 'Musical'),
    ('war', 'War'), ('criminal', 'Criminal'), ('children', 'Children')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_rlmeed', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
