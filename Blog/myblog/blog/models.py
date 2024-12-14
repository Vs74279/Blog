from django.db import models

# Create your models here.
class Category(models.Model):
    Category_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='category/')
    add_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='post/')
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title    
