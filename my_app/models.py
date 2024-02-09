from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='author')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='post')
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Archives(models.Model):
    month = models.CharField(max_length=212)
    count = models.IntegerField()

    def __str__(self):
        return self.month


class About(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='about')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    email = models.EmailField()
    website = models.CharField(max_length=212)
    message = models.TextField(max_length=212)

    def __str__(self):
        return self.name
