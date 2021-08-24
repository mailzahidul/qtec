from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    img = models.ImageField(upload_to='blog/', default='blog/Django_ecommerce-site.png',blank=True,  null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
