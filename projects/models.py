from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=1000)
    cover = models.ImageField(upload_to='thumbnails/%y/%m/%d/')
    logo = models.ImageField(upload_to='logos/%y/%m/%d')
    behance = models.CharField(max_length=10000)

    def __str__(self):
        return self.title
