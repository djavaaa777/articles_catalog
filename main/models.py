from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Article(models.Model):
    title=models.CharField('title',max_length=50)
    preview=models.CharField('preview',max_length=250)
    content=models.TextField('content')
    date=models.DateField('date')

    def __str__(self):
        return self.title
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('content')
    date_created = models.DateTimeField('date',auto_now_add=True)

    def __str__(self):
        return self.content[:50]


