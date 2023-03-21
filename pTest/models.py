from django.db import models

class News(models.Model):
    newsTitle = models.CharField(max_length=128)
    newsAuthor = models.CharField(max_length=128)
    newsDate = models.CharField(max_length=128)
    newsDescription = models.CharField(max_length=128)

    def __str__(self):
        return self.newsTitle