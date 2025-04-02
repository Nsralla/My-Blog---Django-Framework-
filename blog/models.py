from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=50)
    
    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=100, unique=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email_address}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"



class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    excerpt = models.CharField(max_length=200)
    content= models.TextField(validators=[MinLengthValidator(10), MaxLengthValidator(10000)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)
    image_name = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f"{self.title} by {self.author} on {self.date}  "
    
    def get_content(self):
        return self.content[:100] + "..." if len(self.content) > 100 else self.content