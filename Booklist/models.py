from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class BookTask(models.Model):
    user = models.ForeignKey(
        User,null=True,blank=True,on_delete=models.CASCADE)
    cover = models.ImageField(null=True,blank=True,upload_to="static")
    title = models.CharField(max_length=50)
    price = models.FloatField(max_length=20,null=True,blank=True)
    author = models.CharField(max_length=50,null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    book = models.FileField(upload_to="static/book",null=True,max_length=1000)
    complete = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

    def get_absolute_url(self):
        return reverse('index')

    @property

    def imageURL(self):
        try:
            url = self.cover.url
        except:
            url = ''
        return url