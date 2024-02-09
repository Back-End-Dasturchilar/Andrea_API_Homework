from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to='author/')


    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name
    

    

class Post(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='post/')
    category = models.OneToOneField(Category, on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(Category, related_name='tags')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

class MiniPost(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='mini/')
    desc_up = models.TextField()
    desc_bottom = models.TextField()
    mini = models.ForeignKey(Post, on_delete=models.CASCADE)



    def __str__(self):
        return self.title
    

class Comment(models.Model):
    writer = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.writer.name
