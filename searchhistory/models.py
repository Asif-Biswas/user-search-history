from django.db import models

# Create your models here.

class User(models.Model):
    user = models.CharField(max_length=50)

    def __str__(self):
        return self.user
    

class Keyword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_name')
    keyword = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.keyword
