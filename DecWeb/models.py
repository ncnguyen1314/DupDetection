from django.db import models

# Create your models here.
class Pair(models.Model):
    firstSentence = models.CharField(max_length=300)
    secondSentence = models.CharField(max_length=300)
class Result(models.Model):
    Pair = models.ForeignKey(Pair, on_delete = models.CASCADE)
    result = models.CharField(max_length=1)