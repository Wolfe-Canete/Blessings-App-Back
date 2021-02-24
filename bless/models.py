from django.db import models

# Create your models here.
class Blessing(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField(default='Count your blessings.')

    def __str__(self):
        return self.author

class Comment(models.Model):
    commenter = models.CharField(max_length=100)
    blessing = models.ForeignKey(
        Blessing,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField(default='Post comment here!')

    def __str__(self):
        return self.commenter