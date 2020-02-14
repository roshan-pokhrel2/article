from django.db import models

class Articles(models.Model):
    username = models.CharField(max_length=100, default='user')
    title   = models.CharField(max_length=200)
    description = models.TextField(max_length=1000000)
    date = models.DateTimeField()
    image = models.CharField(max_length=100000)

    def __str__(self):
        return self.username

class getintouch(models.Model):

    username = models.CharField(max_length=100, default='user')
    email1   = models.CharField(max_length=100,)
    issue = models.TextField(max_length=1000000)

    def __str__(self):
        return self.email1
    



    
