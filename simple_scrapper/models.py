from django.db import models

# Create your models here.

class ScrapResult(models.Model):
    key = models.CharField(max_length=100, primary_key=True)
    expected = models.IntegerField()
    found = models.IntegerField()
