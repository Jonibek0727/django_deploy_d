from django.db import models

# Create your models here.
class ProductModel(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PostModel(models.Model):
    title1 = models.CharField(max_length=200)
    body = models.TextField()
    pro = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title1