from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Chat(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.name

class Messages(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('message_date',)