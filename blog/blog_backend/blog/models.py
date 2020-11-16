from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # updates only at the creation of record
    created_at = models.DateTimeField(auto_now_add=True)
    # updates every time Model.save() is called
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.title