from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Notice(models.Model):
    title= models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    body=models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
    