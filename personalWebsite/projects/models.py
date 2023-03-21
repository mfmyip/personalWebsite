# Create your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    repo_link = models.CharField(max_length=100, default='https://github.com/mfmyip/')
    image = models.FilePathField(path="projects/static/img/")
    def __str__(self):
        return self.title