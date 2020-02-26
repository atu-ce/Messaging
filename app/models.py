from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Post(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=23, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "t_article"

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = "t_comment"

    def __str__(self):
        return self.text        


class Message(models.Model):
    body = models.TextField()
    sender=models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender_messages")
    receiver=models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver_messages")

    class Meta:
        db_table = "t_message"
        ordering = ["id"]

    def __str__(self):
        return self.body