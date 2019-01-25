from datetime import datetime

from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField


# Create your models here.
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published", default=datetime.now())

    def __str__(self):
        return self.tutorial_title
